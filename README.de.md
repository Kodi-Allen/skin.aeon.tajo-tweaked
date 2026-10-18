# Aeon Tajo Tweaked – klassisches Leia-Home-Menü für Kodi 21 Omega

**Aeon Tajo Tweaked** bringt das klassische **horizontale Home-Menü von Aeon Tajo im Leia-Stil** und seine markante, fette Typografie auf **Kodi 21 (Omega)**. Der eigenständig installierbare Community-Fork von [Aeon Tajo](https://github.com/manfeed/skin.aeon.tajo) verbindet das vertraute Leia-Layout mit dem gepflegten Omega-Quellstand.

[Über das Kodi Allen Repository installieren](https://github.com/Kodi-Allen/kodi-repo#installation) · [Version 1.0.1 herunterladen](https://github.com/Kodi-Allen/skin.aeon.tajo-tweaked/releases/download/v1.0.1/skin.aeon.tajo.tweaked-1.0.1.zip) · [English README](README.md) · [Fehler melden](https://github.com/Kodi-Allen/skin.aeon.tajo-tweaked/issues)

![Aeon Tajo Tweaked mit klassischem horizontalem Leia-Home-Menü unter Kodi 21 Omega](docs/screenshots/aeon-tajo-tweaked-kodi-21-leia-home-menu-tv-shows.jpg)

## Darum gibt es diese Version

Aktuelle Aeon-Tajo-Versionen verwenden ein neueres Home-Menü. Aeon Tajo Tweaked behält die Kodi-21-Omega-Kompatibilität und stellt die frühere Darstellung wieder her:

- Klassisches horizontales Aeon-Tajo-Home-Menü aus der Leia-Zeit.
- Ursprüngliche, fette Menü- und Titelschriften sowie Kiye Sans für Widget-Überschriften.
- Kategoriespezifische Hintergründe und der vertraute, angewinkelte Auswahlrahmen.
- Eigene Add-on-ID `skin.aeon.tajo.tweaked`, daher parallel zum Original installierbar.
- Gepflegte Verbesserungen an Film-, Serien-, Artwork-, Episoden- und Navigationsansichten.
- Normale und kompakte Live-TV-Infobar mit korrektem Abstand für ein- bis vierstellige Sendernummern.

Der Skin ist für 1920 × 1080 im Seitenverhältnis 16:9 ausgelegt. Eine Fernbedienung oder Tastatur wird empfohlen.

## Screenshots der gepflegten Kodi-Installation

Serien | Live TV
--- | ---
![Aeon Tajo Tweaked mit Leia-Serienmenü unter Kodi 21](docs/screenshots/aeon-tajo-tweaked-kodi-21-leia-home-menu-tv-shows.jpg) | ![Aeon Tajo Tweaked mit Leia-Live-TV-Menü unter Kodi 21](docs/screenshots/aeon-tajo-tweaked-kodi-21-leia-home-menu-live-tv.jpg)

Spiele | Vierstellige Live-TV-Sendernummer
--- | ---
![Aeon Tajo Tweaked mit Leia-Spielemenü unter Kodi 21](docs/screenshots/aeon-tajo-tweaked-kodi-21-leia-home-menu-games.jpg) | ![Aeon Tajo Tweaked mit vierstelliger Sendernummer unter Kodi 21](docs/screenshots/aeon-tajo-tweaked-kodi-21-live-tv-infobar-standard.png)

Normale Infobar | Kompakte Infobar
--- | ---
![Normale PVR-Infobar von Aeon Tajo Tweaked unter Kodi 21](docs/screenshots/aeon-tajo-tweaked-kodi-21-live-tv-infobar-standard.png) | ![Kompakte PVR-Infobar von Aeon Tajo Tweaked unter Kodi 21](docs/screenshots/aeon-tajo-tweaked-kodi-21-live-tv-infobar-compact.jpg)

Die Screenshots wurden direkt auf dem gepflegten Vero 4K+ mit Kodi 21.1 aufgenommen. Sie zeigen das wiederhergestellte Home-Layout, die Typografie, Hintergründe und die Live-TV-Infobar dieses Releases. Es werden weder fremde Screenshots noch persönliche Bibliothekseinträge verwendet.

## Version und Kompatibilität

| Versionsreihe | Add-on-ID | Version | Kompatibilität |
| --- | --- | --- | --- |
| Aeon Tajo Tweaked | `skin.aeon.tajo.tweaked` | 1.0.1 | Kodi 21 Omega; mit Kodi 21.1 getestet. |
| Ursprüngliche Aeon-Tajo-Basis | `skin.aeon.tajo` | 7.7.2 | Omega-Basis beim Erstellen des Forks. |

Aeon Tajo Tweaked besitzt eine eigene `1.x`-Versionsreihe. Version 1.0.1 enthält die aktiv gepflegte Arbeit am Leia-Home-Menü und den klassischen Schriften. Der historische Branch `kodi22-leia-gui` war eine Integrationsquelle und ist weder ein eigenes Kodi-22-Release noch eine Kompatibilitätszusage.

## Installation über das Kodi Allen Repository

1. [`repository.kodiallen-1.0.1.zip`](https://raw.githubusercontent.com/Kodi-Allen/kodi-repo/main/repository.kodiallen/repository.kodiallen-1.0.1.zip) herunterladen.
2. In Kodi unter **Einstellungen → System → Add-ons** bei Bedarf **Unbekannte Quellen** aktivieren.
3. **Einstellungen → Add-ons → Aus ZIP-Datei installieren** öffnen und die Repository-ZIP auswählen.
4. **Aus Repository installieren → Kodi Allen Repository → Look and feel → Skin → Aeon Tajo Tweaked** öffnen.
5. **Installieren** wählen und anschließend zum Skin wechseln.

Alternativ kann [`skin.aeon.tajo.tweaked-1.0.1.zip`](https://github.com/Kodi-Allen/skin.aeon.tajo-tweaked/releases/download/v1.0.1/skin.aeon.tajo.tweaked-1.0.1.zip) direkt installiert werden. Das über **Code → Download ZIP** erzeugte GitHub-Archiv ist kein installierbares Kodi-Add-on-Paket.

## Wechsel vom originalen Aeon Tajo

Aeon Tajo Tweaked überschreibt `skin.aeon.tajo` nicht. Beide Skins können installiert bleiben, Kodi speichert ihre Einstellungen jedoch getrennt. Der Tweaked-Skin muss nach dem Wechsel eingerichtet werden.

## Vierstellige Live-TV-Sendernummern

Die normale und kompakte PVR-Infobar reservieren einen eigenen Bereich für die Sendernummer. Vierstellige Nummern wie `2001`, `2900` oder `9002` überlappen weder Sendernamen noch Logo. Lange Sendernamen bleiben scrollbar; Codec-Symbole, EPG-Angaben und Uhrzeit behalten ihre Position.

## Hilfe

[Erstelle ein Issue](https://github.com/Kodi-Allen/skin.aeon.tajo-tweaked/issues) mit Kodi-Version, Betriebssystem, Skin-Version, betroffener Ansicht, Reproduktionsschritten, Screenshot und relevanten Kodi-Logzeilen. Entferne vorher Passwörter, Tokens, API-Schlüssel, Serveradressen, private Pfade und andere persönliche Angaben.

## Danksagung und Lizenz

- **manfeed** — ursprünglicher [Aeon-Tajo-Skin](https://github.com/manfeed/skin.aeon.tajo) und Basisversion 7.7.2 für Omega.
- **BigNoid** — Aeon Nox 5 als Inspiration des Originalskins.
- **frodo19** — Filmgenre-Symbole mit der in `LICENSE.txt` dokumentierten Erlaubnis.
- **Kodi-Allen** — Pflege und Veröffentlichung von Aeon Tajo Tweaked.

Aeon Tajo Tweaked wird unter [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) veröffentlicht. Siehe [`LICENSE.txt`](LICENSE.txt). Einzelne enthaltene Komponenten können abweichende Lizenzbedingungen besitzen.
