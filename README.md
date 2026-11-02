# Filmfriend Kodi Add-on – Kodi 21 Omega & LibreELEC

Use **Filmfriend on Kodi** to watch films and series from participating public
libraries. This independent Filmfriend Kodi add-on is maintained by macsobeck
for Kodi 21 Omega and LibreELEC, with Widevine playback and current
authentication support, including changes affecting Stuttgart Public Library.

[Download the latest Filmfriend release](https://github.com/macsobeck/plugin.video.filmfriend.macsobeck/releases/latest)
· [Installation guide](https://macsobeck.github.io/plugin.video.filmfriend.macsobeck/)

> This is an independent community project and is not affiliated with
> Filmfriend. A valid account at a participating public library is required.

## Features and compatibility

- Watch Filmfriend films and series directly in Kodi
- Supports Kodi 21 Omega, LibreELEC, and Python 3
- Widevine playback through InputStream Adaptive
- English and German user interface
- Participating libraries in Germany, Austria, Switzerland, Liechtenstein,
  Belgium, Luxembourg, and France
- Promptly maintained authentication support, particularly for Stuttgart
  Public Library

## Install the Filmfriend Kodi add-on

1. Download the current Kodi installation file from
   [GitHub Releases](https://github.com/macsobeck/plugin.video.filmfriend.macsobeck/releases/latest).
2. In Kodi, open **Add-ons → Install from zip file** and select the downloaded
   file.
3. Make sure Widevine CDM is configured, for example through the settings of
   the **InputStream Helper** add-on.
4. Open this add-on's settings and select **Login**.
5. Choose your country and library, then sign in with your valid library
   account.

This fork uses the separate add-on ID `plugin.video.filmfriend.macsobeck`.
Repositories containing `plugin.video.filmfriend.de` therefore cannot replace
or update it.

## Move from another Filmfriend add-on

Install this add-on alongside the existing `plugin.video.filmfriend.de` add-on
and start it once. This allows existing settings and tokens to be migrated.
Verify login and playback before disabling or removing the former add-on.

## Login and playback help

- **“Login has expired”:** Install the latest version, then sign in again from
  the add-on settings.
- **Video does not start:** Check that InputStream Adaptive and Widevine CDM
  are configured.
- **Library is missing or login fails:** Open a
  [GitHub issue](https://github.com/macsobeck/plugin.video.filmfriend.macsobeck/issues)
  and include your Kodi version, operating system, and library. Never publish
  passwords or tokens.

## History and licensing

This is an independent maintenance fork of Ingo-FP-Angel's
`plugin.video.filmfriend.de`. It was created so that authentication changes
required by Stuttgart Public Library can be handled promptly. Historical
attribution does not imply active ownership or an update relationship.

The add-on is licensed under GPL-2.0-only. See `LICENSE-NOTICE.md` for a
plain-language summary and `LICENSE.txt` for the controlling license text.

## Development

Architecture, authentication and token lifecycle, Filmfriend endpoints,
Widevine playback, migration behavior, and Kodi 21/LibreELEC risks are
documented in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

Run the tests without Kodi:

```sh
python3 -m unittest discover -s tests -v
```
