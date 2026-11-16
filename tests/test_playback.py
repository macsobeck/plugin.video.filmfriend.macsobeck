# SPDX-License-Identifier: GPL-2.0-only

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "plugin.video.filmfriend.macsobeck"))

from resources.lib.playback import (  # noqa: E402
    media_state_fields,
    widevine_properties,
)


class PlaybackTests(unittest.TestCase):
    def test_media_state_fields_are_optional_and_credential_safe(self):
        self.assertEqual(
            ("Active", True),
            media_state_fields({
                "state": {"kind": "Active", "isPinRequired": True},
            }),
        )
        self.assertEqual((None, None), media_state_fields({"state": None}))
        self.assertEqual((None, None), media_state_fields(None))

    def test_kodi_21_widevine_properties_use_one_drm_interface(self):
        props = widevine_properties("https://license.example.test/wv")

        self.assertEqual(
            {"inputstream.adaptive.drm_legacy"},
            set(props),
        )
        self.assertIn(
            "com.widevine.alpha|https://license.example.test/wv|",
            props["inputstream.adaptive.drm_legacy"],
        )
        self.assertIn(
            "Content-Type=application%2Foctet-stream",
            props["inputstream.adaptive.drm_legacy"],
        )


if __name__ == "__main__":
    unittest.main()
