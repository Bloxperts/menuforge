# Personalization Fields — Cold-Email Pipeline

Pipeline-Inputs für `template_de_v1.md`. Jede gesendete E-Mail muss alle Felder gefüllt haben — fehlt eines, wird der Empfänger übersprungen, nicht mit Fallback-Müll versendet.

| Field | Required | Source | Format / Constraints | Beispiel |
|---|---|---|---|---|
| `{{salutation}}` | yes | derived from `{{owner_gender}}` | `Herr` \| `Frau` (kein „Herr/Frau"-Slash) | `Frau` |
| `{{owner_last_name}}` | yes | Webseite Impressum, Handelsregister, Google Business | Nachname only, korrekt geschrieben (Umlaute beachten). **Wenn unbekannt: Empfänger SKIP**, kein generisches Fallback. | `Müller` |
| `{{restaurant_name}}` | yes | Scraper-Hauptfeld | Wie das Restaurant sich selbst nennt — inkl. „Restaurant", „Beizli", „zur" etc. | `Restaurant zur Sonne` |
| `{{city}}` | yes | Scraper | Schweizer Stadt/Gemeinde, ohne Kanton-Suffix. | `Adliswil` |
| `{{compliment_one_line}}` | yes | manuell oder LLM aus Webseite/Reviews | 1 Halbsatz, konkret + ehrlich. Verbietet leere Floskeln. Max 12 Wörter. | `bekannt für Ihre Älplermagronen und die Terrasse mit Sihlblick` |
| `{{what_we_changed}}` | yes | Pipeline (aus Redesign-Schritt) | 1 Halbsatz, beschreibt eine konkrete Änderung — keine Buzzwords. Max 15 Wörter. | `klarere Schrift-Hierarchie und Fokus auf Ihre drei meistbestellten Gerichte` |
| `{{teaser_url}}` | yes | Pipeline-Output | HTTPS-Link, eindeutig pro Restaurant, ohne Login. Slug-basiert, keine UTM-Tracking-Parameter im sichtbaren Link. | `https://menuforge.ch/t/sonne-adliswil` |
| `{{landing_url}}` | yes | konstant | Globale Landing-URL der CEO-Signatur. | `menuforge.ch` |

## Validierungsregeln (Pipeline)

1. **Hard skip** wenn `{{owner_last_name}}` leer/unsicher. Kein „Sehr geehrte Damen und Herren"-Fallback — das verbrennt das Restaurant für später.
2. **Soft skip** (Restaurant in „needs review"-Bucket) wenn `{{compliment_one_line}}` oder `{{what_we_changed}}` aus dem Generator floskelhaft sind (Heuristik: enthält „toll", „super", „modern", „frisch", „zeitgemäss" ohne Substantiv).
3. **`{{teaser_url}}` muss vor Versand HEAD-200 zurückgeben.** Pipeline pingt Link, sonst Versand-Abort.
4. **Encoding:** UTF-8, deutsche Umlaute ungeschadet (ä/ö/ü/ß→ss). Test: rendert `Müller` korrekt im Subject und Body.

## Out of scope für dieses Spec

- Gender-Detection-Logik (`{{owner_gender}}`) — separates Ticket.
- `{{compliment_one_line}}`-Generator (manuell für die ersten 20, dann LLM-assisted).
- Mehrsprachige Varianten (FR/IT) — Phase 2.
