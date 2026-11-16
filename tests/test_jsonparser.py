# SPDX-License-Identifier: GPL-2.0-only

import sys
import types
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "plugin.video.filmfriend.macsobeck"))


class FakeAddon:
    def getAddonInfo(self, key):
        return {
            "id": "plugin.video.filmfriend.macsobeck",
            "name": "Filmfriend",
        }.get(key, "")


class FakeLogger:
    def __init__(self):
        self.events = []

    def info(self, event, **fields):
        self.events.append((event, fields))

    def warning(self, *args, **kwargs):
        self.events.append((args[0], kwargs))

    def error(self, *args, **kwargs):
        pass


xbmcaddon = types.ModuleType("xbmcaddon")
xbmcaddon.Addon = lambda *args, **kwargs: FakeAddon()
sys.modules["xbmcaddon"] = xbmcaddon
sys.modules.setdefault("xbmcgui", types.ModuleType("xbmcgui"))

external = types.ModuleType("resources.lib.external")
external.__path__ = [str(
    ROOT / "plugin.video.filmfriend.macsobeck" / "resources" / "lib" /
    "external")]
sys.modules["resources.lib.external"] = external

lm4utils = types.ModuleType(
    "resources.lib.external.libmediathek4utils")
lm4utils.getSetting = lambda key: "en" if key == "language" else ""
lm4utils.getTranslation = lambda string_id: string_id
lm4utils.displayMsg = lambda title, message: None
sys.modules["resources.lib.external.libmediathek4utils"] = lm4utils
external.libmediathek4utils = lm4utils

kodi_runtime = types.ModuleType("resources.lib.kodi_runtime")
kodi_runtime.build_runtime = lambda language: (
    None, FakeLogger(), None, None, None)
sys.modules["resources.lib.kodi_runtime"] = kodi_runtime

import resources.lib.jsonparser as jsonparser  # noqa: E402
from resources.lib.jsonparser import parseResponse  # noqa: E402


class JsonParserEdgeCaseTests(unittest.TestCase):
    def test_non_active_metadata_still_probes_authoritative_uri(self):
        class Api:
            def __init__(self):
                self.uri_requests = []

            def media_details(self, media_type, video_id):
                return {
                    "state": {
                        "kind": "UnexpectedAuthenticatedState",
                        "isPinRequired": False,
                    },
                }

            def media_uri(self, media_type, video_id):
                self.uri_requests.append((media_type, video_id))
                return {
                    "mpegDash": "https://media.example.test/video.mpd",
                    "widevineLicenseServerUri":
                        "https://license.example.test/widevine",
                }

        api = Api()
        logger = FakeLogger()
        original_api = jsonparser._api
        original_logger = jsonparser._logger
        try:
            jsonparser._api = api
            jsonparser._logger = logger
            result = jsonparser.getVideoUrl("movie-id")
        finally:
            jsonparser._api = original_api
            jsonparser._logger = original_logger

        self.assertEqual([("movies", "movie-id")], api.uri_requests)
        self.assertEqual(
            "https://media.example.test/video.mpd",
            result["media"][0]["url"],
        )
        self.assertIn(
            ("playback.media_state", {
                "media_type": "movies",
                "pin_required": False,
                "state_kind": "UnexpectedAuthenticatedState",
            }),
            logger.events,
        )

    def test_geo_blocked_metadata_does_not_trigger_token_refresh(self):
        class Api:
            def __init__(self):
                self.uri_requests = []

            def media_details(self, media_type, video_id):
                return {
                    "state": {
                        "kind": "GeoBlocked",
                        "isPinRequired": None,
                    },
                }

            def media_uri(self, media_type, video_id):
                self.uri_requests.append((media_type, video_id))
                raise AssertionError("GeoBlocked media must not request /uri")

        api = Api()
        logger = FakeLogger()
        messages = []
        original_api = jsonparser._api
        original_logger = jsonparser._logger
        original_display = jsonparser.lm4utils.displayMsg
        original_translation = jsonparser.lm4utils.getTranslation
        try:
            jsonparser._api = api
            jsonparser._logger = logger
            jsonparser.lm4utils.displayMsg = (
                lambda title, message: messages.append((title, message)))
            jsonparser.lm4utils.getTranslation = lambda string_id: string_id
            result = jsonparser.getVideoUrl("movie-id")
        finally:
            jsonparser._api = original_api
            jsonparser._logger = original_logger
            jsonparser.lm4utils.displayMsg = original_display
            jsonparser.lm4utils.getTranslation = original_translation

        self.assertEqual([], api.uri_requests)
        self.assertEqual({"media": []}, result)
        self.assertEqual([(30606, 30607)], messages)
        self.assertIn(
            ("playback.geo_blocked", {"media_type": "movies"}),
            logger.events,
        )

    def test_season_survives_missing_series_and_season_number(self):
        page = parseResponse({
            "results": [{
                "kind": "Season",
                "result": {
                    "id": "season-id",
                    "englishTitle": "Fallback title",
                    "artworkUris": [],
                },
            }],
        }, content="tvshows")

        self.assertEqual(1, len(page["items"]))
        metadata = page["items"][0]["metadata"]
        self.assertEqual("Fallback title", metadata["name"])
        self.assertEqual([], metadata["genres"])
        self.assertNotIn("season", metadata)

    def test_season_survives_null_genres(self):
        page = parseResponse({
            "results": [{
                "kind": "Season",
                "result": {
                    "id": "season-id",
                    "seasonNumber": 2,
                    "series": {
                        "englishTitle": "Example series",
                        "genres": None,
                    },
                    "artworkUris": [],
                },
            }],
        }, content="tvshows")

        metadata = page["items"][0]["metadata"]
        self.assertEqual("Example series - Season 2", metadata["name"])
        self.assertEqual(2, metadata["season"])
        self.assertEqual([], metadata["genres"])

    def test_episode_survives_null_nested_season_and_genres(self):
        page = parseResponse({
            "results": [{
                "kind": "Episode",
                "result": {
                    "id": "episode-id",
                    "englishTitle": "Example episode",
                    "episodeNumber": 4,
                    "runtime": 1800,
                    "season": None,
                    "genres": None,
                    "artworkUris": [],
                },
            }],
        }, content="episodes")

        metadata = page["items"][0]["metadata"]
        self.assertEqual(4, metadata["episode"])
        self.assertNotIn("season", metadata)
        self.assertEqual([], metadata["genres"])


if __name__ == "__main__":
    unittest.main()
