# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-only
"""Kodi 21 InputStream Adaptive property construction."""

import urllib.parse


def media_state_fields(details):
    """Return credential-safe availability fields from media details."""
    if not isinstance(details, dict):
        return None, None
    state = details.get("state")
    if not isinstance(state, dict):
        return None, None

    state_kind = state.get("kind")
    if not isinstance(state_kind, str) or not state_kind:
        state_kind = None
    pin_required = state.get("isPinRequired")
    if not isinstance(pin_required, bool):
        pin_required = None
    return state_kind, pin_required


def widevine_properties(license_url):
    headers = urllib.parse.urlencode({
        "Content-Type": "application/octet-stream",
    })
    return {
        # Kodi 21 / inputstream.adaptive 21.5+ simple DRM interface. Do not
        # combine this with license_type/license_key: ISA rejects mixed DRM
        # configuration before initializing the encrypted stream.
        "inputstream.adaptive.drm_legacy":
            f"com.widevine.alpha|{license_url}|{headers}",
    }
