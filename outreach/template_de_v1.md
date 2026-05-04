# MenuForge — Cold-Email Template DE v1

**Status:** v1, ready to send. Voice approved by CEO. Plain text only at this stage.
**Locale:** Schweiz (DACH-Phase 1). Hochdeutsch mit Schweizer Konventionen (CHF, „ss" statt „ß", „Grüezi"). Optionaler Mundart-Variant unten.
**Length:** Body ~120 Wörter, mobil lesbar, genau 1 Link.
**Sender:** Roland (CEO, MenuForge). Eine Person, kein Team-„wir".

---

## Subject lines (A/B/C)

A — Neugier, lokal:
> Eine Idee für die Speisekarte vom {{restaurant_name}}

B — konkret, Mehrwert:
> Vorschau: Ihre Karte vom {{restaurant_name}} neu gestaltet

C — kurz, persönlich:
> Kleines Geschenk für {{restaurant_name}}

Default für ersten Schwung: **A**. B/C als A/B-Test ab Volumen ≥ 50 Empfänger.

---

## Body — Hochdeutsch (Schweizer Konventionen)

```
Grüezi {{salutation}} {{owner_last_name}},

beim Recherchieren in {{city}} bin ich auf das {{restaurant_name}} gestossen — {{compliment_one_line}}. Was mir aufgefallen ist: die Speisekarte wirkt online weniger einladend als das, was bei Ihnen auf den Tisch kommt.

Statt nur zu schreiben, habe ich es kurzerhand gemacht. Eine Seite Ihrer Karte habe ich neu gestaltet — als Vorschau, nichts Verpflichtendes:

{{teaser_url}}

Konkret: {{what_we_changed}}.

Falls Ihnen die Richtung gefällt, gestalte ich die komplette Karte für CHF 390 (einmalig, druckfertig, eine Korrekturrunde inbegriffen). Kein Abo, keine versteckten Kosten.

Antworten Sie einfach mit „Interesse" — ich schicke die volle Version. Oder wir telefonieren 10 Minuten, Sie wählen den Slot.

Herzliche Grüsse aus Zürich
Roland
MenuForge · {{landing_url}}
```

Word count (body, ohne Anrede/Signatur): ~125.

---

## Body — Mundart-Variant (Züritüütsch, optional)

Nur einsetzen für: sehr kleine, familiengeführte Beizen ohne offizielle Webseite, ländliche Lage (Kt. ZH/BE/AG/TG). Im Zweifel Hochdeutsch nehmen — Mundart in Schriftform kann bei städtischen oder gehobenen Lokalen unprofessionell wirken.

```
Grüezi {{salutation}} {{owner_last_name}},

bim Rächerchiere in {{city}} isch mer s'{{restaurant_name}} ufgfalle — {{compliment_one_line}}. Was mer ufgfalle isch: d'Spyysichaarte wirkt online weniger iiladend als das, wo bi Ihne uf de Tisch chunnt.

Statt nur z'schriibe, hani's churzerhand gmacht. Ei Site vo Ihrer Charte hani neu gstaltet — als Vorschou, nüt Verpflichtends:

{{teaser_url}}

Konkret: {{what_we_changed}}.

Falls Ihne d'Richtig gfallt, gstaltn i d'ganzi Charte für CHF 390 (einmalig, druckfärtig, ei Korrekturrundi dezue). Kei Abo, kei versteckti Chöste.

Antwortet eifach mit „Interesse" — i schick Ihne d'volli Version. Oder mir telefonieren 10 Minute, Sie wähled de Slot.

Härzliche Grüess us Züri
Roland
MenuForge · {{landing_url}}
```

---

## Send-Checklist (vor jedem Versand)

- [ ] `{{teaser_url}}` öffnet sich auf Mobil ohne Login, lädt < 2s.
- [ ] `{{owner_last_name}}` verifiziert (Handelsregister oder Webseite-Impressum). Kein „Sehr geehrte Damen und Herren" — wenn kein Name auffindbar, Restaurant überspringen oder Anrede „an das Team vom {{restaurant_name}}".
- [ ] `{{compliment_one_line}}` ist konkret und ehrlich (z.B. „bekannt für Ihre hausgemachten Maultaschen", nicht „tolles Restaurant").
- [ ] `{{what_we_changed}}` benennt eine konkrete Designentscheidung, kein Marketing-Sprech.
- [ ] Genau 1 Link im Body. Keine Tracking-Parameter, die wie Spam aussehen (`?utm_…` vermeiden, lieber Pfad-Slug).
- [ ] Aus Gmail von Roland's persönlicher Adresse senden, nicht von `noreply@`.
- [ ] Keine Anhänge.

## Out of scope (separate Tickets)

- Send-Infrastruktur, Bounce-Handling, Throttling.
- Follow-up-Sequenz (Tag 4, Tag 10).
- HTML-Variante (erst wenn Plain-Text-Reply-Rate validiert ist).
