# MenuForge Pipeline

This directory contains the pipeline for processing restaurant menus into professional teasers.

## Pipeline Stages

1. **Ingest**: Input is a PDF, JPG, or PNG of an existing menu
2. **Extract**: OCR + structure detection → list of `{section, item_name, description?, price?}`
3. **Section pick**: auto-pick the section with the most items, or accept a CLI flag to choose
4. **Redesign render**: apply our HTML/CSS template to the chosen section
5. **Before/after capture**: screenshot the original and our rendered teaser
6. **Output**: 
   - `out/<slug>/teaser.pdf` (A4, side-by-side before/after, ready to attach)
   - `out/<slug>/preview.html` (mobile-friendly hosted version, just the redesigned section)
   - `out/<slug>/meta.json` (slug, restaurant name, source path, section name, created_at)

## Usage

```bash
python pipeline/run.py --input <path-to-menu> --slug <unique-slug>
```

## Requirements

- pdfplumber (for PDF parsing)
- pytesseract (for image OCR)
- weasyprint (for HTML to PDF)
- jinja2 (for templating)

## Quality Standards

The example output must be:
- Sendable to a real restaurant without being embarrassed
- Pricing column aligned, no broken characters
- No OCR garbage ("Q ur 2,50" etc.)
- Typography is modern and consistent
- Mobile preview opens cleanly on a phone