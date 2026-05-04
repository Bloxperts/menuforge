# MenuForge Design System

> MenuForge sells premium menu redesign. The landing page IS the product demo.
> If it looks generic, we lose the sale before the restaurant reads a word.
> Every design decision must earn trust from a restaurant owner who judges
> quality with their eyes first.

---

## Design Reference

**Primary inspiration:** https://mont-fort.com/
Study it. Notice: dark backdrop, generous whitespace, confident typography,
no decorative clutter. Authority is communicated through restraint, not embellishment.

**Secondary references:**
- https://www.noma.dk/ — how a food brand earns premium perception
- https://www.ottolenghi.co.uk/ — editorial typography applied to food
- https://www.collect.com/ — clean before/after product showcase

---

## Brand Personality

MenuForge is a **design studio that happens to be automated**.
Tone: confident, minimal, European. Not startup-cheerful. Not agency-jargon.
A restaurant owner should feel: "these people know what good looks like."

---

## Color Palette

```
--color-bg:          #161412   /* Near-black with warm undertone — not cold */
--color-surface:     #1E1B18   /* Cards, sections */
--color-border:      #2E2A25   /* Subtle separators */
--color-accent:      #C4973A   /* Warm gold — premium, food-adjacent */
--color-accent-muted:#8A6A28   /* Hover states, secondary accent */
--color-text:        #F0EBE3   /* Warm off-white — not pure #fff */
--color-text-muted:  #8C8279   /* Secondary text, captions */
--color-paper:       #F5F0E8   /* For menu preview areas only */
```

Never use: generic Bootstrap blue, flat gray (#888), pure black (#000), pure white (#fff).

---

## Typography

**Display / Hero headings**
- Font: `Cormorant Garamond` (Google Fonts, weight 300–500)
- Used for: H1, H2, large pull quotes
- Character: editorial, magazine-quality, timeless serif
- Size: H1 ≥ 4rem desktop, ≥ 2.6rem mobile

**Body / UI**
- Font: `DM Sans` (Google Fonts, weight 300–400)
- Used for: all body text, nav, buttons, captions
- Size: body 1rem / 1.6 line-height minimum

**Forbidden:** Roboto, Bootstrap default stack, system-ui as primary, Comic Sans (obviously).

Load both from Google Fonts:
```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500&family=DM+Sans:wght@300;400&display=swap" rel="stylesheet">
```

---

## Layout Principles

1. **Full-viewport hero.** First section = 100vh. No content below the fold on load.
2. **Generous whitespace.** Section padding ≥ 6rem top/bottom. Never cramped.
3. **One thing per section.** Hero, How it works, Before/After, Pricing, CTA.
   Each section makes one argument. Resist adding a second.
4. **Before/After is the hero feature.** Not a bullet list — real side-by-side images
   with a clear quality gap. This is the product demo. Invest here.
5. **Mobile-first.** Design for 375px, scale up. Check every section at 375px.
6. **No stock-photo smiles.** Use food/table/texture photography only.
   Good free sources: Unsplash (search "restaurant interior", "menu", "table setting").

---

## Component Patterns

### Buttons
```css
/* Primary CTA */
background: var(--color-accent);
color: #161412;
font-family: 'DM Sans';
font-weight: 400;
letter-spacing: 0.08em;
text-transform: uppercase;
font-size: 0.8rem;
padding: 1rem 2.5rem;
border: none;
border-radius: 0;  /* No rounded corners — crisp, confident */

/* Secondary / Ghost */
background: transparent;
border: 1px solid var(--color-accent);
color: var(--color-accent);
```

### Section Headers
```css
.section-label {  /* Small label above heading */
  font-family: 'DM Sans';
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--color-accent);
  margin-bottom: 1rem;
}
h2 {
  font-family: 'Cormorant Garamond';
  font-weight: 300;
  font-size: clamp(2rem, 5vw, 3.5rem);
  color: var(--color-text);
  line-height: 1.15;
}
```

### Before / After Preview
- Side by side at desktop, stacked at mobile
- Left: photo of a real (bad) handwritten or Word-generated menu
- Right: the redesigned MenuForge version — clean typography, hierarchy, visual appeal
- Label each side clearly: "Vorher" / "Nachher" in small DM Sans uppercase
- The quality difference must be *obvious* at a glance

---

## Imagery

- **Hero background:** full-bleed restaurant interior or table detail, dark-tinted
  (CSS: `filter: brightness(0.4)` over a Unsplash photo)
- **Before menu:** use `data/` folder examples, or a realistic low-quality placeholder
- **After menu:** use the pipeline output from Task B, or a clean typeset placeholder
- **No illustrations, no icons packs, no emoji in headings**

---

## Animation / Motion

- Fade-in on scroll for sections: `opacity: 0 → 1`, `translateY(20px → 0)`, duration 0.6s
- No bouncing, spinning, or parallax — restraint signals quality
- Hover on CTA button: accent color darkens slightly, no scale transforms

---

## Acceptance Criteria — Design Review Checklist

A page passes design review when ALL of the following are true:

- [ ] Hero is full viewport height with background image, dark overlay, Cormorant Garamond H1
- [ ] Gold accent color (`#C4973A`) is used consistently; no Bootstrap blue visible
- [ ] Both fonts (Cormorant + DM Sans) are loaded and visibly applied
- [ ] Before/After section shows real visual contrast — not a bullet list
- [ ] No rounded buttons (border-radius: 0 on primary CTA)
- [ ] Section padding ≥ 6rem — page breathes, is not cramped
- [ ] Screenshot at 375px looks intentional, nothing overlaps or overflows
- [ ] Background is dark (`#161412` or close), not white or light gray
- [ ] No generic placeholder blue anywhere
- [ ] "Impressum" and "Datenschutz" links exist in footer

---

## What Failure Looks Like

Reject and iterate if you see any of the following:
- Blue `#007bff` or `#0d6efd` anywhere → Bootstrap default crept in
- White background with dark text as the primary color scheme
- Rounded pill buttons
- Generic sans-serif heading (Arial, Roboto, system-ui)
- Bullet-point "how it works" instead of numbered visual steps
- Section padding < 4rem
- Hero that doesn't fill the screen
- Mobile layout that clips or overflows
