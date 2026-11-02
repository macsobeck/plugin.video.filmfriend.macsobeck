---
title: "Install the Filmfriend Kodi Add-on – Kodi 21 & LibreELEC"
description: "Install Filmfriend on Kodi 21 Omega and LibreELEC, sign in through your public library, configure Widevine, and stream films and series."
---

# Filmfriend for Kodi 21 Omega and LibreELEC

This independent **Filmfriend Kodi add-on** lets you watch films and series
from participating public libraries directly in Kodi. Maintained by macsobeck,
the fork supports Kodi 21 Omega, LibreELEC, Widevine playback, and current
authentication flows, including changes affecting Stuttgart Public Library.

[**Download the latest Filmfriend release**](https://github.com/macsobeck/plugin.video.filmfriend.macsobeck/releases/latest)

A valid account at a participating public library is required. This is an
independent community project and is not affiliated with Filmfriend.

## Install the Filmfriend Kodi add-on

1. Download the current Kodi installation file from
   [GitHub Releases](https://github.com/macsobeck/plugin.video.filmfriend.macsobeck/releases/latest).
2. In Kodi, open **Add-ons → Install from zip file**.
3. Select the downloaded ZIP and wait for Kodi to confirm the installation.
4. Configure Widevine CDM if needed, for example through the settings of
   **InputStream Helper**.
5. Open the add-on settings, select **Login**, and sign in through your public
   library.

## Supported systems and countries

The add-on is designed for Kodi 21 Omega, LibreELEC, and Python 3. Its user
interface is available in English and German. It supports participating
libraries in Germany, Austria, Switzerland, Liechtenstein, Belgium, Luxembourg,
and France.

## Stuttgart Public Library support

This fork is maintained independently so that changes to the Stuttgart Public
Library authentication process can be handled promptly. If login fails, first
install the
[latest release](https://github.com/macsobeck/plugin.video.filmfriend.macsobeck/releases/latest),
then start a new login from the add-on settings.

## Move from another Filmfriend add-on

If you use `plugin.video.filmfriend.de`, install this add-on alongside it and
start the new add-on once. This allows existing settings and tokens to be
migrated. Verify login and playback before disabling or removing the former
add-on.

The new add-on has its own ID, `plugin.video.filmfriend.macsobeck`, and is
updated separately.

## Frequently asked questions

### Does Filmfriend work with Kodi 21 Omega?

Yes. This fork is designed for Kodi 21 Omega and playback through InputStream
Adaptive with Widevine.

### Can I use Filmfriend on LibreELEC?

Yes. LibreELEC is a supported environment. Widevine CDM must be configured for
protected video playback.

### What should I do when “Login has expired” appears?

Install the current add-on release, then sign in to your library again from the
add-on settings.

### Do I need a library card?

You need valid access to a participating public library. Contact your library
to learn whether access is available and which conditions apply.

### Is this an official Filmfriend add-on?

No. It is an independent, open-source community project and is not affiliated
with Filmfriend.

## Source code and support

[View the source code or report a problem on GitHub](https://github.com/macsobeck/plugin.video.filmfriend.macsobeck).

Released under GPL-2.0-only.
