# MenuForge Outreach & Reply-Handling Playbook

Operator manual for running the first-10-teasers cycle end-to-end. A non-founder should be able to read this top-to-bottom and execute the next cycle without asking questions.

Phase 1 target: **10 teasers sent → 1+ verbal yes** (definition in §7).

This playbook covers Day 4 follow-up, Day 10 final ping, reply triage, the booking call, and the tracker. The Day 0 cold email body is defined in [`template_de_v1.md`](./template_de_v1.md) — do not duplicate it here. If template_de_v1 and this file disagree on D0 mechanics (subject, pricing, delivery format), the **template wins**.

Locale baseline: Switzerland-first (CHF 390, Hochdeutsch with Swiss conventions). DE/AT variants use the same playbook but adjust currency and salutation.

---

## 1. Cycle overview

| Day | Action | Channel | Owner |
|-----|--------|---------|-------|
| 0   | Send cold email per `template_de_v1.md` (subject A by default; body includes teaser URL and CHF 390 firm price) | Email | Operator |
| 4   | Gentle nudge ("haben Sie den Entwurf gesehen?") | Reply on D0 thread | Operator |
| 10  | Final ping with a different angle (seasonal / social-proof / specific-problem) | Reply on D0 thread | Operator |
| 14  | If still silent, mark `no_reply` and stop. Re-add to next cohort in ~90 days. | Tracker only | Operator |

Rules:
- All three touches stay in the **same email thread**. Never start a new subject line.
- Send Tue–Thu, 09:30–11:00 local time. Avoid Mondays and Fridays.
- One follow-up per day max per restaurant. If they reply, jump to reply triage (§5) and stop the schedule.

---

## 2. Day 0 — Teaser send

Use `template_de_v1.md`. Run the send-checklist in that file before each send. Three things to capture into the tracker the moment the email goes out:
- `restaurant`, `cohort`, `sent_at` (ISO timestamp), `next_action=nudge_d4`.

Do **not** restate the price, attach a PDF, or add a Cal.com link — the template's URL-based, single-price, "reply with Interesse OR pick a 10-min call slot" structure is the version we are testing in this cohort.

---

## 3. Day 4 — Gentle nudge

Reply *on the same thread*. One short paragraph.

Template (DE, Swiss conventions):

```
Kurzes Nachfassen — haben Sie den Entwurf gesehen? Würde mich freuen
zu hören, was Sie davon halten, auch wenn es ein klares "nein, passt
nicht" ist.

Herzliche Grüsse
Roland
```

Update tracker: `next_action=final_ping_d10`.

---

## 4. Day 10 — Final ping with a different angle

Switch the angle. Don't ask "what do you think" again — give them a *new* reason to reply.

Pick one of these, in order of preference based on context:

**A. Seasonal hook** (default for May–Oct send window):
```
Letzter Versuch von meiner Seite. Da bei vielen Häusern jetzt die
{{seasonal, z.B. Spargel-/Sommer-/Herbst-}}karte ansteht: wenn Sie
den Entwurf für die neue Saison nutzen wollen, mache ich Ihnen die
saisonale Anpassung gratis dazu.

Sonst lasse ich Sie in Ruhe.

Roland
```

**B. Social-proof hook** (use once we have ≥1 paying customer):
```
Letzter Versuch. {{reference_restaurant}} hat den Entwurf vor kurzem
übernommen — falls hilfreich, schicke ich Ihnen das Vorher/Nachher.

Sonst lasse ich Sie in Ruhe.

Roland
```

**C. Specific-problem hook** (use when the original menu had an obvious flaw):
```
Letzter Versuch. Mir ist beim Vergleich aufgefallen, dass {{specific_observation,
z.B. "die Vorspeisen auf der aktuellen Karte schwer auffindbar sind"}} —
genau das löst der Entwurf. Falls relevant, freue ich mich über eine
kurze Rückmeldung.

Roland
```

Update tracker: `next_action=close_no_reply`. If no reply by D14, flip to `no_reply`.

---

## 5. Reply triage — 4 buckets

When a reply lands, classify into exactly one bucket within 1 business day. Reply same-day if possible.

### Bucket 1: `interested`
Signal: any positive language ("schön", "gefällt mir", "interessant", "Interesse", asks about timeline/next steps), or a clean "ja, bitte volle Version schicken".

Response template (DE):
```
Freut mich sehr! Hier die komplette Version Ihrer Karte als PDF
(druckfertig): {{full_version_url_or_attachment}}.

Wenn Sie loslegen wollen: ich brauche von Ihnen nur Ihr OK auf das
1-Seiten-Angebot, das ich Ihnen heute Abend zuschicke. Lieferung
der finalen Datei dann innert 5 Werktagen, mit einer Korrekturrunde.

Falls vor dem Angebot noch Fragen offen sind, telefonieren wir
10 Minuten — zwei Vorschläge:
- {{slot_1, z.B. Mi 14:00}}
- {{slot_2, z.B. Do 10:30}}

Herzliche Grüsse
Roland
```

Rules:
- Lead with the asset (full version), not the call. The teaser worked — give them more of it.
- Two manual slots, not Cal.com (we don't have one yet, and a cold reply doesn't need self-serve).
- Update tracker: `response_bucket=interested`, `next_action=send_offer`.

### Bucket 2: `pricing_question`
Signal: pushback or detail-ask on price. *"CHF 390 — was ist genau drin?"*, *"geht's auch günstiger?"*, *"wir haben mehrere Karten"*.

Response template (DE):
```
Gerne, kurz und transparent:

Im Preis von CHF 390 enthalten:
- Komplette Neugestaltung Ihrer Karte (alle Seiten der bestehenden
  Karte, eine Sprache).
- Druckfertige PDF-Datei plus Online-Version.
- Eine Korrekturrunde.
- Lieferung innert 5 Werktagen nach Auftrag.

Zusätzliche Sprachen oder eine Saisonkarte oben drauf: je CHF 90.
Mehrere komplett unterschiedliche Karten (z.B. Mittag/Abend separat):
schaue ich mir an und nenne Ihnen einen Festpreis vorab.

Wenn das passt, antworten Sie einfach mit "ja" — ich schicke das
1-Seiten-Angebot heute Abend. Wenn Sie es vorher kurz besprechen
wollen, hier zwei Slots:
- {{slot_1}}
- {{slot_2}}

Herzliche Grüsse
Roland
```

Rules:
- Always confirm the CHF 390 anchor first (it was in D0). Never lower it without scope reduction.
- Add-ons are itemised, not negotiated.
- Update tracker: `response_bucket=pricing_question`, `next_action=send_offer_or_book_call`.

### Bucket 3: `not_now`
Signal: "aktuell keine Zeit", "vielleicht später", "nicht dieses Quartal", "wir denken darüber nach".

Response template (DE):
```
Verstanden, danke für die Rückmeldung. Ich melde mich in ca.
{{N, default 3}} Monaten nochmal kurz — passt das?

Den Entwurf können Sie natürlich behalten.

Herzliche Grüsse
Roland
```

Update tracker: `response_bucket=not_now`, `next_action=requeue_+90d`, set follow-up reminder.

### Bucket 4: `unsubscribe`
Signal: "kein Interesse", "bitte nicht mehr schreiben", "abmelden", silence-with-anger ("hören Sie auf").

Response template (DE):
```
Alles klar, ich nehme Sie aus der Liste. Vielen Dank und alles
Gute weiterhin.

Roland
```

Hard rules:
- Add the email + restaurant to `data/suppression.csv` (create if missing) the same day.
- Never re-contact, including different cohorts, different campaigns, different team members.
- Update tracker: `response_bucket=unsubscribe`, `next_action=suppress_permanent`.

---

## 6. Booking flow — landing the 10-minute call

Most replies should not need a call — the D0 email already disclosed the price (CHF 390) and the offer. A call is for *price questions, scope edge cases, or buyers who want to hear a human voice before committing*.

### Before the call
- Re-read the original D0 email and the teaser URL (2 min).
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
- Re-state CHF 390 firm, what's in it (per `pricing_question` template), what's an add-on.
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

A verbal yes requires **all three** of the following, captured during or immediately after the call (or by email if no call happened):

1. **Explicit affirmative** to the close question or to the offer email. Examples that count:
   - "Ja, machen wir."
   - "Passt, schicken Sie das Angebot."
   - "Okay, lass uns das so machen."
   - On email: "Ja" / "Auftrag bestätigt" / "Bitte loslegen" in reply to the 1-page offer.
   Examples that do **not** count:
   - "Klingt interessant" (without commitment)
   - "Ich denke darüber nach"
   - "Schicken Sie mal Infos" (without scope agreement)

2. **Price acknowledgment.** The owner has seen the firm price (CHF 390 plus any agreed add-ons) and either explicitly accepted it or did not push back when it was re-stated. If they say "muss ich überlegen" on price, it is *not* a verbal yes yet.

3. **A concrete next step with a date.** Either:
   - A delivery date for the final menu, OR
   - A signed-offer commitment ("ich unterschreibe das Angebot bis {{date}}").

If any of the three is missing, status is `interested-warm`, not `verbal_yes`. Continue working it, but do not count it toward the Phase 1 goal.

---

## 8. Tracker

File: `outreach/runs/log.csv`. One row per restaurant per cohort.

Schema (CSV header):
```
restaurant,cohort,sent_at,response_at,response_bucket,next_action,verbal_yes,notes
```

Field rules:
- `restaurant`: human-readable name + city, e.g. `Restaurant Sonne, Winterthur`.
- `cohort`: integer, monotonically increasing per send-batch (Phase 1 starts at `1`).
- `sent_at`, `response_at`: ISO-8601 with time, e.g. `2026-05-04T10:15+02:00`.
- `response_bucket`: one of `interested | pricing_question | not_now | unsubscribe | no_reply`. Empty until a reply lands or D14 passes.
- `next_action`: one of `nudge_d4 | final_ping_d10 | close_no_reply | send_offer | send_offer_or_book_call | book_call | requeue_+90d | suppress_permanent | done_won | done_lost`. Never empty for >24h on an open row.
- `verbal_yes`: `true | false`. Only flip to `true` when all three §7 criteria are met.
- `notes`: free text. Always include verbatim close-quote if a call happened, plus the specific observation logged before the call.

Update cadence:
- Same day for any send, reply, or call.
- End-of-week: review all `next_action` values, queue Monday's work.
- End-of-cohort (after D14 of the last send): tally results, note in `outreach/runs/cohort_{{N}}_summary.md` (one paragraph: sent / replied / by-bucket / verbal-yes count / lessons).

---

## 9. Operator FAQ

**Q: They replied from a different email address (e.g. an assistant). Who do I follow up with?**
A: Reply to whoever wrote, but address the original owner by name. Mark in `notes`.

**Q: They asked for the editable file (InDesign / Word).**
A: Decline politely until paid. Template: *"Die finale Datei liefere ich nach Beauftragung — die Vorschau bleibt aber selbstverständlich bei Ihnen."*

**Q: They forwarded to a chain HQ.**
A: Bucket as `not_now`, set `notes=chain_HQ_referred`, requeue +180 days, do not chase HQ cold.

**Q: They want a phone call instead of email reply.**
A: Treat as `interested`, propose 2 manual slots directly in the next reply.

**Q: I sent the wrong teaser link / wrong restaurant in the body.**
A: Reply within 1 hour: *"Entschuldigung, falscher Link — hier die richtige Vorschau für {{restaurant}}: {{teaser_url}}."* Do not start a new thread.

**Q: They reply only to ask which restaurant we mean (multiple branches).**
A: Treat as `interested`, ask which branch they want first, redo the teaser for that branch only, restart the cycle from D0 for that specific branch.

**Q: The price scares them off (`pricing_question` reply that's clearly a "too expensive" signal).**
A: Do not lower CHF 390. Instead, offer a smaller scope: *"Falls die ganze Karte zu viel ist — wir können auch nur die Hauptseite (Speisen) machen, für CHF 190. Getränke- und Dessertkarten bleiben wie sie sind."* If that's still no, bucket as `not_now`.
