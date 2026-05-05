# MenuForge Landing Site

Plain static HTML for `menuforge.ch`. No build step. Drop the contents of this folder onto any static host (Cloudflare Pages, Netlify, GitHub Pages, plain nginx, S3+CloudFront).

## Local dev

```
cd landing
npm run dev    # → http://127.0.0.1:8080
```

(Wraps `python3 -m http.server 8080` — no Node dependencies installed, the package.json is just a script shim.)

## Files

| File | Purpose |
|---|---|
| `index.html` | Public landing page. German hero copy, 3 reasons, offer block, CTA = mailto:roland@menuforge.ch. |
| `preview.html` | Template for `/preview/<slug>` shell. The MEN-8 pipeline produces per-restaurant copies of this file with the redesigned menu section baked in. |
| `impressum.html` | Required Swiss legal page. **Contains placeholders** — Roland must fill in postal address / handelsregister / UID before public schaltung. |
| `datenschutz.html` | revDSG + DSGVO-aware privacy notice. **Recommend a lawyer/specialist review** before public schaltung, especially if contacting EU restaurants. |
| `styles.css` | One stylesheet, ~150 lines. Inter for body, Lora for headings (system fallbacks if web fonts not loaded). Mobile-first, no framework, no CDN dependency. |
| `example-teaser.png` | Referenced from `index.html` in the example section. **Not yet committed** — needs an actual before/after screenshot from the pipeline once the first real teaser is rendered. |

## Deploy options (Phase 1, simplest first)

1. **Cloudflare Pages** — drag-and-drop `landing/` directory. Free tier covers Phase 1 traffic. Custom domain `menuforge.ch` configurable.
2. **GitHub Pages** — push this directory as a separate branch (`gh-pages`) or use Actions to deploy from `landing/` on push to main.
3. **Netlify** — same as #1.

Pick based on Roland's existing accounts. No hosting decision baked in yet.

## Customization before first send

Before sending the **first real outreach email**, Roland must:

1. Replace `roland@menuforge.ch` (mailto links in `index.html`, `impressum.html`, `datenschutz.html`, `preview.html`) with the real From address if it differs.
2. Fill in `impressum.html` placeholders (Postadresse, ggf. Handelsregister, ggf. UID/MWST).
3. Replace `example-teaser.png` with a real before/after screenshot from a successful pipeline run.
4. Decide hosting domain and deploy.
5. Bless the German copy in `index.html` (in particular the hero + 3 reasons) — or hand back to CEO to revise.

## Preview slug deployment (interim)

For Phase 1, the simplest deploy of per-restaurant previews is:

```
landing/
  index.html
  preview/
    sonne-adliswil/
      index.html      # = preview.html with content + restaurant_name baked in
      teaser.pdf      # downloadable, optional
    zentralhof-zh/
      index.html
      teaser.pdf
    ...
```

The MEN-8 pipeline's output (`out/<slug>/preview.html`) becomes `landing/preview/<slug>/index.html` after a simple wrapper substitution. We do this as a build step for now; Phase 3 swaps it for a real server.

## Out of scope

- Multi-language site (English / French / Italian). Phase 2 if relevant.
- CMS / admin panel. We don't need it for 10 teasers/week.
- Cookie banner. None set, none needed.
- Web analytics. Intentionally absent — keeps the privacy story simple.
