# MenuForge Outreach & Reply-Handling Playbook

Operator manual for running the first-10-teasers cycle end-to-end. A non-founder should be able to read this top-to-bottom and execute the next cycle without asking questions.

Phase 1 target: **10 teasers sent → 1+ verbal yes** (definition at the bottom).

---

## 1. Cycle overview

| Day | Action | Channel | Owner |
|-----|--------|---------|-------|
| 0   | Send teaser email (with PDF attached + 1 inline preview image) | Email | Operator |
| 4   | Gentle nudge ("did you see your teaser?") | Reply on D0 thread | Operator |
| 10  | Final ping with a different angle (seasonal hook) | Reply on D0 thread | Operator |
| 11+ | Mark `no_reply` and stop. Re-add to next cohort in ~90 days. | Tracker only | Operator |

Rules:
- All three touches stay in the **same email thread**. Never start a new subject line.
- Send Tue–Thu, 09:30–11:00 local time. Avoid Mondays and Fridays.
- One follow-up per day max per restaurant. If they reply, jump to reply triage and stop the schedule.

---

## 2. Day 0 — Teaser send

Goal: get the owner to open the PDF and feel "wow, this is *my* menu, but better."

Subject line (DE): `Ihre Speisekarte – ein Vorschlag von uns`
Subject line (DE, formal AT/CH variant): `Vorschlag für Ihre Speisekarte`

Body template (DE):

```
Guten Tag {{owner_first_name_or_team}},

wir haben uns Ihre aktuelle Speisekarte angeschaut und einen Vorschlag
erstellt, wie sie moderner und verkaufsstärker aussehen könnte.

Der Entwurf hängt als PDF an – kostenlos, unverbindlich, nur als Idee.

Wenn es Ihnen gefällt, können wir die finale Version in unter einer
Woche liefern. Wenn nicht, behalten Sie den Entwurf einfach.

Beste Grüße
{{sender_name}}
MenuForge
```

Hard rules for D0:
- Attach the PDF teaser. File name: `{{restaurant_slug}}_menuforge.pdf`.
- Inline-embed **one** preview page (the strongest one) so it renders in Outlook/Apple Mail previews.
- No price in the email. Price comes only on the call or after explicit ask.
- No Cal.com link in the first email. We want a reply, not a self-serve booking from a cold contact.

Log immediately in `outreach/runs/log.csv`:
- `restaurant`, `sent_at`, `next_action=nudge_d4`.

---

## 3. Day 4 — Gentle nudge

Reply *on the same thread*. Keep it to one short paragraph.

Template (DE):

```
Kurzes Nachfassen – haben Sie den Entwurf gesehen? Würde mich freuen
zu hören, was Sie davon halten, auch wenn es ein klares "nein, passt
nicht" ist.

{{sender_name}}
```

Update tracker: `next_action=final_ping_d10`.

---

## 4. Day 10 — Final ping with a different angle

Switch the angle. Don't ask "what do you think" again — give them a *new* reason to reply.

Pick one of these, in order of preference based on context:

**A. Seasonal hook** (default for May–Oct send window):
```
Letzter Versuch von meiner Seite. Da die Spargel-/Sommer-/Herbstkarte
jetzt für viele Häuser ansteht: wenn Sie den Entwurf für die neue
Saison nutzen wollen, mache ich Ihnen die Anpassung gratis dazu.

Sonst lasse ich Sie in Ruhe.

{{sender_name}}
```

**B. Social-proof hook** (use once we have ≥1 paying customer):
```
Letzter Versuch. {{reference_restaurant}} hat den Entwurf vor kurzem
übernommen – falls hilfreich, schicke ich Ihnen das Vorher/Nachher.

Sonst lasse ich Sie in Ruhe.

{{sender_name}}
```

**C. Specific-problem hook** (use when the original menu had an obvious flaw):
```
Letzter Versuch. Mir ist beim Vergleich aufgefallen, dass {{specific_observation,
e.g. "die Vorspeisen auf der aktuellen Karte schwer auffindbar sind"}} –
genau das löst der Entwurf. Falls relevant, freue ich mich über ein
kurzes Feedback.

{{sender_name}}
```

Update tracker: `next_action=close_no_reply` (will flip to `no_reply` if D14 passes silent).

---

## 5. Reply triage — 4 buckets

When a reply lands, classify into exactly one bucket within 1 business day. Reply same-day if possible.

### Bucket 1: `interested`
Signal: any positive language ("schön", "gefällt mir", "interessant", "wie geht es weiter", asks about timeline or next steps).

Response template (DE):
```
Freut mich sehr! Lassen Sie uns 10 Minuten telefonieren – dann
zeige ich Ihnen kurz, wie wir die finale Version liefern und was
es kostet.

Hier können Sie direkt einen Slot wählen: {{cal_com_link}}

Falls Cal.com bei Ihnen nicht funktioniert, hier zwei Vorschläge:
- {{slot_1, z.B. Mi 14:00}}
- {{slot_2, z.B. Do 10:30}}

{{sender_name}}
```

Update tracker: `response_bucket=interested`, `next_action=book_call`.

### Bucket 2: `pricing_question`
Signal: "was kostet das?", "wie teuer", any direct price ask before a call is booked.

Response template (DE):
```
Klar, kurz und ehrlich:
- Einmalige Neugestaltung Ihrer Karte: {{price_band, z.B. 290–490 €}},
  je nach Umfang (Anzahl Seiten, Bilder, Sprachen).
- Druckdaten und Online-PDF inklusive.

Wenn Sie wollen, schaue ich mir Ihre konkrete Karte an und nenne
Ihnen die genaue Zahl in einem 10-Minuten-Call:
{{cal_com_link}}

{{sender_name}}
```

Rules:
- Always give a *band*, never a single number, before the call.
- Always close with the booking link.
- Update tracker: `response_bucket=pricing_question`, `next_action=book_call`.

### Bucket 3: `not_now`
Signal: "aktuell keine Zeit", "vielleicht später", "nicht dieses Quartal", "wir denken darüber nach".

Response template (DE):
```
Verstanden, danke für die Rückmeldung. Ich melde mich in ca.
{{N, default 3}} Monaten nochmal kurz – passt das?

Den Entwurf können Sie natürlich behalten.

{{sender_name}}
```

Update tracker: `response_bucket=not_now`, `next_action=requeue_+90d`, set follow-up reminder.

### Bucket 4: `unsubscribe`
Signal: "kein Interesse", "bitte nicht mehr schreiben", "abmelden", silence-with-anger ("hören Sie auf").

Response template (DE):
```
Alles klar, ich nehme Sie aus der Liste. Vielen Dank und alles
Gute weiterhin.

{{sender_name}}
```

Hard rules:
- Add the email + restaurant to `data/suppression.csv` (create if missing) the same day.
- Never re-contact, including different cohorts, different campaigns, different team members.
- Update tracker: `response_bucket=unsubscribe`, `next_action=suppress_permanent`.

---

## 6. Booking flow — landing the 10-minute call

### Before the call
- Re-read the original teaser PDF and the email thread (2 min).
- Look up the restaurant: opening hours, current menu online (if different from the one we worked from), Google rating count, average review length. Note one specific observation.
- Confirm the call slot 24h before via the same email thread.

### On the call (10 minutes, hard cap)

Open (1 min):
> "Danke für die Zeit. Ich halte mich an 10 Minuten. Kurz gefragt: Was hat Sie am Entwurf am meisten angesprochen?"

Three questions to ask, in this order:

1. **Pain question** (2 min):
   > "Wenn Sie an Ihre aktuelle Karte denken — was nervt Sie selbst am meisten daran?"
   *Listen for: outdated, no photos, hard to update, looks unprofessional, languages missing.*

2. **Decision-maker question** (1 min):
   > "Entscheiden Sie selbst über die Karte, oder ist da noch jemand involviert?"
   *If "noch jemand": ask name + role, and propose a follow-up that includes them.*

3. **Timeline question** (1 min):
   > "Wenn wir das machen — wann bräuchten Sie die fertige Karte?"
   *Listen for: a date, an event, a season change, "irgendwann" (= weak signal).*

Pitch (2 min):
- Show what changes between the teaser and the final version (resolution, print-ready, your photos, your edits).
- Quote a single number inside the band you gave by email. Be specific.
- Offer one concrete next step: *"Ich schicke Ihnen heute Abend ein 1-Seiten-Angebot. Wenn Sie zustimmen, liefere ich die finale Karte bis {{date}}."*

Close (2 min):
- Ask: *"Passt das für Sie so?"*
- Wait. Do not fill silence.
- Capture answer verbatim in tracker.

### After the call
Within 2 hours:
- Send the 1-page offer (PDF) on the same email thread.
- Update tracker: `response_bucket`, `verbal_yes` flag, `notes` with verbatim close-quote.

---

## 7. What counts as a "verbal yes" (Phase 1 definition)

A verbal yes requires **all three** of the following, captured during or immediately after the call:

1. **Explicit affirmative** to the close question. Examples that count:
   - "Ja, machen wir."
   - "Passt, schicken Sie das Angebot."
   - "Okay, lass uns das so machen."
   Examples that do **not** count:
   - "Klingt interessant" (without commitment)
   - "Ich denke darüber nach"
   - "Schicken Sie mal Infos" (without scope agreement)

2. **Price acknowledgment.** The owner has heard a specific number (not just a band) and did not push back, OR explicitly accepted it. If they say "muss ich überlegen" on price, it is *not* a verbal yes.

3. **A concrete next step with a date.** Either:
   - A delivery date for the final menu, OR
   - A signed-offer commitment ("ich unterschreibe das Angebot bis {{date}}").

If any of the three is missing, status is `interested-warm`, not `verbal_yes`. Continue working it, but do not count it toward the Phase 1 goal.

---

## 8. Tracker

File: `outreach/runs/log.csv`. One row per restaurant per cohort. See schema header in the CSV.

Update cadence:
- Same day for any send, reply, or call.
- End-of-week: review all `next_action` values, queue Monday's work.
- End-of-cohort (after Day 14 of the last send): tally results, note in `outreach/runs/cohort_{{N}}_summary.md`.

Do not let a row sit with `next_action=` empty for >24h. If it's empty, the cycle has stalled.

---

## 9. Operator FAQ

**Q: They replied from a different email address (e.g. an assistant). Who do I follow up with?**
A: Reply to whoever wrote, but address the original owner by name. Mark in `notes`.

**Q: They asked for the editable file (InDesign / Word).**
A: Decline politely until paid. Template: *"Die finale Datei liefere ich nach Beauftragung — der Entwurf bleibt aber selbstverständlich bei Ihnen."*

**Q: They forwarded to a chain HQ.**
A: Bucket as `not_now`, set `notes=chain_HQ_referred`, requeue +180 days, do not chase HQ cold.

**Q: They want a phone call instead of email reply.**
A: Treat as `interested`, but skip Cal.com link — propose 2 slots directly.

**Q: I sent the wrong PDF.**
A: Reply within 1 hour: *"Entschuldigung, falsche Datei — hier der richtige Entwurf für {{restaurant}}."* Do not start a new thread.
