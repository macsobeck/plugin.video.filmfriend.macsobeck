# Filmfriend-Kodi-Add-on – Kodi 21 Omega & LibreELEC

[English](README.md) | Deutsch

Mit **Filmfriend auf Kodi** können Sie Filme und Serien teilnehmender
öffentlicher Bibliotheken ansehen. Dieses unabhängige Filmfriend-Kodi-Add-on
wird von macsobeck für Kodi 21 Omega und LibreELEC gepflegt. Es unterstützt
Widevine-Wiedergabe und aktuelle Anmeldeverfahren einschließlich der
Änderungen, die die Stadtbibliothek Stuttgart betreffen.

[Neueste Filmfriend-Version herunterladen](https://github.com/macsobeck/plugin.video.filmfriend.macsobeck/releases/latest)
· [Installationsanleitung](https://macsobeck.github.io/plugin.video.filmfriend.macsobeck/)

> Dies ist ein unabhängiges Community-Projekt und steht in keiner Verbindung
> zu Filmfriend. Ein gültiges Konto bei einer teilnehmenden öffentlichen
> Bibliothek ist erforderlich.

## Funktionen und Kompatibilität

- Filmfriend-Filme und -Serien direkt in Kodi ansehen
- Unterstützt Kodi 21 Omega, LibreELEC und Python 3
- Widevine-Wiedergabe über InputStream Adaptive
- Englische und deutsche Benutzeroberfläche
- Teilnehmende Bibliotheken in Deutschland, Österreich, der Schweiz,
  Liechtenstein, Belgien, Luxemburg und Frankreich
- Zeitnah gepflegte Anmeldeunterstützung, insbesondere für die
  Stadtbibliothek Stuttgart

## Filmfriend-Kodi-Add-on installieren

1. Laden Sie die aktuelle Kodi-Installationsdatei unter
   [GitHub Releases](https://github.com/macsobeck/plugin.video.filmfriend.macsobeck/releases/latest)
   herunter.
2. Öffnen Sie in Kodi **Add-ons → Aus ZIP-Datei installieren** und wählen Sie
   die heruntergeladene Datei aus.
3. Stellen Sie sicher, dass Widevine CDM eingerichtet ist, zum Beispiel über
   die Einstellungen des Add-ons **InputStream Helper**.
4. Öffnen Sie die Einstellungen dieses Add-ons und wählen Sie **Anmelden**.
5. Wählen Sie Ihr Land und Ihre Bibliothek und melden Sie sich mit Ihrem
   gültigen Bibliothekskonto an.

Dieser Fork verwendet die separate Add-on-ID
`plugin.video.filmfriend.macsobeck`. Repositorys, die
`plugin.video.filmfriend.de` enthalten, können ihn daher weder ersetzen noch
aktualisieren.

## Von einem anderen Filmfriend-Add-on wechseln

Installieren Sie dieses Add-on neben dem vorhandenen
`plugin.video.filmfriend.de`-Add-on und starten Sie es einmal. Dadurch können
vorhandene Einstellungen und Token übernommen werden. Prüfen Sie Anmeldung und
Wiedergabe, bevor Sie das frühere Add-on deaktivieren oder entfernen.

## Hilfe bei Anmeldung und Wiedergabe

- **„Anmeldung abgelaufen“:** Installieren Sie die neueste Version und melden
  Sie sich anschließend in den Add-on-Einstellungen erneut an.
- **Video startet nicht:** Prüfen Sie, ob InputStream Adaptive und Widevine CDM
  eingerichtet sind.
- **Bibliothek fehlt oder Anmeldung schlägt fehl:** Erstellen Sie ein
  [GitHub-Issue](https://github.com/macsobeck/plugin.video.filmfriend.macsobeck/issues)
  und nennen Sie Ihre Kodi-Version, Ihr Betriebssystem und Ihre Bibliothek.
  Veröffentlichen Sie niemals Passwörter oder Token.

## Geschichte und Lizenz

Dies ist ein unabhängig gepflegter Fork von Ingo-FP-Angels
`plugin.video.filmfriend.de`. Er wurde erstellt, damit die für die
Stadtbibliothek Stuttgart erforderlichen Änderungen am Anmeldeverfahren zeitnah
umgesetzt werden können. Die historische Namensnennung bedeutet weder eine
aktuelle Eigentümerschaft noch eine Update-Beziehung.

Das Add-on steht unter der Lizenz GPL-2.0-only. Eine leicht verständliche
Zusammenfassung finden Sie in `LICENSE-NOTICE.md`; der maßgebliche Lizenztext
steht in `LICENSE.txt`.

## Entwicklungsunterstützung

Dieses Repository wird von macsobeck mit Unterstützung von OpenAI Codex für
Codeanalyse, Implementierung, Tests, Dokumentation und Release-Vorbereitung
entwickelt und gepflegt. Alle Änderungen werden vom Repository-Betreiber
geprüft und veröffentlicht.

## Entwicklung

Architektur, Anmeldung und Token-Lebenszyklus, Filmfriend-Endpunkte,
Widevine-Wiedergabe, Migrationsverhalten sowie Risiken für Kodi 21 und
LibreELEC sind in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) dokumentiert.

Tests können ohne Kodi ausgeführt werden:

```sh
python3 -m unittest discover -s tests -v
```
