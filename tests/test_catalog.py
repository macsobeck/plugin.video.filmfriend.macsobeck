# SPDX-License-Identifier: GPL-2.0-only

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "plugin.video.filmfriend.macsobeck"))

from resources.lib.catalog import (  # noqa: E402
    genre_records,
    nested_season_number,
    release_date_metadata,
)


class CatalogMetadataTests(unittest.TestCase):
    def test_genre_records_accept_valid_entries_only(self):
        valid = {"name": "Drama"}

        self.assertEqual(
            (valid,),
            genre_records({"genres": [valid, None, "invalid"]}),
        )

    def test_genre_records_ignore_missing_null_and_malformed_lists(self):
        for container in (
                None, {}, {"genres": None}, {"genres": "Drama"}):
            with self.subTest(container=container):
                self.assertEqual((), genre_records(container))

    def test_nested_season_number_accepts_a_mapping(self):
        self.assertEqual(3, nested_season_number({"seasonNumber": 3}))

    def test_nested_season_number_ignores_incomplete_metadata(self):
        for season in (None, {}, "Season 3", []):
            with self.subTest(season=season):
                self.assertIsNone(nested_season_number(season))

    def test_iso_release_date_is_translated_to_kodi_metadata(self):
        self.assertEqual(
            {
                "year": "2026",
                "premiered": "2026-11-01",
                "aired": "2026-11-01",
            },
            release_date_metadata("2026-11-01T12:34:56Z"),
        )

    def test_null_release_date_is_ignored(self):
        self.assertEqual({}, release_date_metadata(None))

    def test_empty_or_malformed_release_date_is_ignored(self):
        for value in ("", "   ", "unknown"):
            with self.subTest(value=value):
                self.assertEqual({}, release_date_metadata(value))


if __name__ == "__main__":
    unittest.main()
