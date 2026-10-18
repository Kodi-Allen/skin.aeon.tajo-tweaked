# Aeon Tajo Tweaked – Skin für Kodi 21 (Omega)

**Aeon Tajo Tweaked** ist ein eigenständiger Community-Fork von [Aeon Tajo](https://github.com/manfeed/skin.aeon.tajo) für **Kodi 21 (Omega)**. Der Skin behält die artwork-orientierte Heimkino-Oberfläche bei und verbessert Film- und Serienansichten, Episodeninformationen, Navigation sowie die **Live-TV- und PVR-Infobar**.

[Über das Kodi Allen Repository installieren](https://github.com/Kodi-Allen/kodi-repo#installation) · [Version 1.0.0 herunterladen](https://github.com/Kodi-Allen/skin.aeon.tajo-tweaked/releases/download/v1.0.0/skin.aeon.tajo.tweaked-1.0.0.zip) · [English README](README.md) · [Fehler melden](https://github.com/Kodi-Allen/skin.aeon.tajo-tweaked/issues)

![Aeon Tajo Tweaked unter Kodi 21 mit vierstelliger Sendernummer in der Live-TV-Infobar](docs/screenshots/aeon-tajo-tweaked-kodi-21-live-tv-infobar-standard.png)

## Funktionen und Verbesserungen

- Eigenständiges Kodi-Add-on mit der ID `skin.aeon.tajo.tweaked`; parallel zum originalen Aeon Tajo installierbar.
- Verbesserte Film- und Serien-Artworks, darunter Clearlogos in der Flix-Ansicht.
- Episodennummern im Format `SxxExx`, aufgeräumte Überschriften und verbesserte Laufzeitangaben.
- Keine leeren Staffel-Metadaten und Episodenstatistiken.
- Überarbeitete Videoinformationen und Media-Cases einschließlich eines Cache-Helfers für unscharfe Hintergründe.
- Normale und kompakte Live-TV-Infobar mit sauberem Platz für ein- bis vierstellige Sendernummern.
- Auf einem Vero 4K+ mit Kodi 21.1 getestet.

Der Skin ist für 1920 × 1080 im Seitenverhältnis 16:9 ausgelegt. Eine Fernbedienung oder Tastatur wird empfohlen; die Maussteuerung funktioniert möglicherweise nicht in jeder Ansicht vollständig.

## Screenshots

Normale Live-TV-Infobar | Kompakte Live-TV-Infobar
--- | ---
![Normale PVR-Infobar von Aeon Tajo Tweaked unter Kodi 21](docs/screenshots/aeon-tajo-tweaked-kodi-21-live-tv-infobar-standard.png) | ![Kompakte PVR-Infobar von Aeon Tajo Tweaked unter Kodi 21](docs/screenshots/aeon-tajo-tweaked-kodi-21-live-tv-infobar-compact.jpg)

Filmbibliothek | Flix-Filmansicht
--- | ---
![Aeon Tajo Filmbibliothek mit Cover-Artwork und Medieninformationen](resources/screenshot-01.jpg) | ![Aeon Tajo Flix-Ansicht mit Filmplakaten und Metadaten](resources/screenshot-02.jpg)

Die Dateien `resources/screenshot-*.jpg` stammen aus der Aeon-Tajo-Basis und zeigen deren allgemeines Design. Die konkrete Darstellung hängt von Metadaten, Artwork, Helfer-Add-ons und den gewählten Skin-Einstellungen ab.

## Version und Kompatibilität

| Branch | Add-on-ID | Version | Status |
| --- | --- | --- | --- |
| [`omega`](https://github.com/Kodi-Allen/skin.aeon.tajo-tweaked/tree/omega) | `skin.aeon.tajo.tweaked` | 1.0.0 | Hauptversion für Kodi 21 (Omega), getestet mit Kodi 21.1. |
| [`kodi22-leia-gui`](https://github.com/Kodi-Allen/skin.aeon.tajo-tweaked/tree/kodi22-leia-gui) | Alte Entwicklungs-ID | 7.7.4 | Experimenteller Branch; gehört nicht zu Version 1.0.0 und garantiert keine Kodi-22-Kompatibilität. |

Version 1.0.0 basiert auf dem `omega`-Quellstand von Aeon Tajo 7.7.2. Der neue Name, die eigene Add-on-ID und die eigene Versionsreihe trennen diesen Fork eindeutig vom Original.

## Installation über das Kodi Allen Repository

1. [`repository.kodiallen-1.0.1.zip`](https://raw.githubusercontent.com/Kodi-Allen/kodi-repo/main/repository.kodiallen/repository.kodiallen-1.0.1.zip) herunterladen.
2. In Kodi unter **Einstellungen → System → Add-ons** bei Bedarf **Unbekannte Quellen** aktivieren.
3. **Einstellungen → Add-ons → Aus ZIP-Datei installieren** öffnen und die Repository-ZIP auswählen.
4. **Aus Repository installieren → Kodi Allen Repository → Look and feel → Skin → Aeon Tajo Tweaked** öffnen.
5. **Installieren** auswählen und anschließend zum neuen Skin wechseln.

Alternativ kann [`skin.aeon.tajo.tweaked-1.0.0.zip`](https://github.com/Kodi-Allen/skin.aeon.tajo-tweaked/releases/download/v1.0.0/skin.aeon.tajo.tweaked-1.0.0.zip) direkt installiert werden. Das über **Code → Download ZIP** erzeugte GitHub-Archiv ist keine installierbare Kodi-Add-on-ZIP.

## Wechsel vom originalen Aeon Tajo

Aeon Tajo Tweaked überschreibt `skin.aeon.tajo` nicht. Beide Skins können gleichzeitig installiert bleiben. Kodi speichert deren Einstellungen jedoch getrennt; der neue Skin muss daher nach dem Wechsel eingerichtet werden.

## Korrektur der Live-TV-Infobar

Die normale und kompakte PVR-Infobar reservieren einen eigenen Bereich für die Sendernummer. Vierstellige Nummern wie `2001`, `2900` oder `9002` überlappen den Sendernamen nicht mehr. Lange Sendernamen bleiben scrollbar; Senderlogo, Codec-Symbole, EPG-Angaben und Uhrzeit behalten ihre Position.

Die Änderung wurde als XML validiert und auf Kodi 21.1 während laufender Live-TV-Wiedergabe in beiden Infobar-Varianten visuell geprüft.

## Hilfe und Fehlerberichte

[Erstelle ein Issue](https://github.com/Kodi-Allen/skin.aeon.tajo-tweaked/issues) mit Kodi-Version, Betriebssystem, Skin-Version, betroffener Ansicht, Reproduktionsschritten, Screenshot und relevanten Kodi-Logzeilen. Entferne vorher Passwörter, Tokens, Serveradressen und andere private Angaben.

## Danksagung und Lizenz

- **manfeed** — ursprünglicher [Aeon-Tajo-Skin](https://github.com/manfeed/skin.aeon.tajo) und Basisversion 7.7.2 für Omega.
- **BigNoid** — Aeon Nox 5 als Inspiration des Originalskins.
- **frodo19** — Filmgenre-Symbole mit der in `LICENSE.txt` dokumentierten Erlaubnis.
- **Kodi-Allen** — Pflege und Veröffentlichung von Aeon Tajo Tweaked.

Aeon Tajo Tweaked wird unter [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) veröffentlicht. Siehe [`LICENSE.txt`](LICENSE.txt). Einzelne enthaltene Komponenten können abweichende Lizenzbedingungen besitzen.
