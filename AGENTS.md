# Arbeitsregeln fuer diesen Skin

- Aenderungen am Skin immer in beiden Pfaden eintragen:
  - Git-Arbeitskopie: `C:\Users\Flo\Documents\Kodi Development\Kodi\skins\skin.aeon.tajo-tweaked-fresh`
  - Installierte Kodi-Kopie: `C:\Users\Flo\AppData\Roaming\Kodi\addons\skin.aeon.tajo`
- Nach XML-Aenderungen nach Moeglichkeit beide betroffenen Dateien kurz auf gueltiges XML pruefen.
- Die installierte Kodi-Kopie ist die Version, die Kodi beim Testen direkt laedt.
- Wenn die installierte Kopie lokale Zusatzanpassungen hat, Dateien nicht blind von Git nach Kodi kopieren, sondern gezielt in beiden Pfaden patchen.
- Der alte Direct-Play-Button `control id="90008"` / `script.kodiallen.directdiscplay` ist obsolet und soll nicht wieder eingebaut werden.
- Gebaute oder gespeicherte Skin-ZIPs immer direkt in `C:\Users\Flo\Documents\Kodi Development\Kodi\skins` ablegen, nicht in Skin-Unterordnern. Eindeutig benennen, z.B. `skin.aeon.tajo-7.7.2-kodi-omega.zip`.
- Das OSMC-Geraet unter `192.168.68.150` laeuft aktuell mit Kodi 20.5 Nexus, nicht Omega. Dafuer eine eindeutig benannte ZIP `skin.aeon.tajo-7.7.2-kodi20-nexus-osmc.zip` bauen; nur im ZIP-`addon.xml` `xbmc.gui` auf `5.16.0` senken. Die Arbeitskopie bleibt unveraendert.
- Kodi 22 Pfade: `ListItem.FileNameAndPath` ist der volle Pfad inklusive Datei und darf nicht direkt mit Artwork-Dateinamen wie `back.jpg` kombiniert werden. Fuer Video-DB-Items zuerst `ListItem.Art(type)` bzw. `Container(id).ListItem.Art(type)` verwenden; wenn ein Dateifallback noetig ist, eher `ListItem.Path` bzw. `Container(id).ListItem.Path` plus Dateiname.
- Video-Info-Blur laeuft ueber `scripts/video_info_blur_cache.py`: der Helper setzt gecachte TMDbHelper-Blur-Dateien direkt und ruft TMDbHelper nur bei Cache-Miss auf.

## Arbeitsteilung Opus / Sonnet

- **Opus plant, Sonnet fuehrt aus.** Bei jeder nicht-trivialen Skin-Aenderung (mehr als 1-2 Zeilen, mehrere Dateien, neue Features, Refactors):
  1. Opus liest betroffene Dateien, identifiziert exakte Zeilen/Stellen, formuliert den detaillierten Schritt-fuer-Schritt-Plan (Pfade, Zeilennummern, alte/neue Strings, Sync-Targets).
  2. Opus delegiert die reine Ausfuehrung per `Agent`-Tool an einen Sonnet-Subagent (`subagent_type: "general-purpose"`, `model: "sonnet"`).
  3. Sonnet-Prompt muss self-contained sein: vollstaendige Pfade, exakter Edit-Wortlaut, Hinweis auf CRLF-Gotcha bei XMLs, Sync nach AppData, kurze Erfolgsmeldung.
  4. Opus prueft das Ergebnis (Diff, XML-Validitaet) und meldet dem User zurueck.
- Triviale Eintaktaenderungen (1 Zeile Edit, kein Sync-Konflikt) darf Opus direkt erledigen.
- Wenn der User explizit "mach das selber" / "ohne Sonnet" sagt, gilt die Regel nicht.
