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
    def warning(self, *args, **kwargs):
        pass

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
sys.modules["resources.lib.external.libmediathek4utils"] = lm4utils
external.libmediathek4utils = lm4utils

kodi_runtime = types.ModuleType("resources.lib.kodi_runtime")
kodi_runtime.build_runtime = lambda language: (
    None, FakeLogger(), None, None, None)
sys.modules["resources.lib.kodi_runtime"] = kodi_runtime

from resources.lib.jsonparser import parseResponse  # noqa: E402


class JsonParserEdgeCaseTests(unittest.TestCase):
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
