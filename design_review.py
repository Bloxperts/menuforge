#!/usr/bin/env python3
"""
MenuForge Design Review Script
Usage: python3 design_review.py [url_or_file] [screenshot_out.png]
Checks HTML against DESIGN.md acceptance criteria and takes a screenshot.
"""
import sys, re, subprocess, os, json

TARGET = sys.argv[1] if len(sys.argv) > 1 else "file:///home/bloxperts/menuforge/index.html"
SCREENSHOT = sys.argv[2] if len(sys.argv) > 2 else "/home/bloxperts/menuforge/design-review-screenshot.png"
DESIGN_MD = "/home/bloxperts/menuforge/DESIGN.md"

# ── 1. Read HTML ─────────────────────────────────────────────────────���────────
if TARGET.startswith("file://"):
    html_path = TARGET[7:]
    with open(html_path) as f:
        html = f.read()
elif TARGET.startswith("http"):
    import urllib.request
    html = urllib.request.urlopen(TARGET).read().decode("utf-8", errors="replace")
else:
    with open(TARGET) as f:
        html = f.read()

html_lower = html.lower()

# ── 2. Run acceptance checklist ───────────────────────────────────────────────
checks = []

def check(label, passed, detail=""):
    checks.append({"label": label, "passed": passed, "detail": detail})

# Fonts
check("Cormorant Garamond loaded",
      "cormorant" in html_lower,
      "Google Fonts link or @import for Cormorant Garamond not found")

check("DM Sans loaded",
      "dm sans" in html_lower or "dm+sans" in html_lower,
      "Google Fonts link or @import for DM Sans not found")

# Colors — gold accent present, no bootstrap blue
check("Gold accent color present (#C4973A or similar)",
      bool(re.search(r'c4973a|c49|b8943f|gold', html_lower)),
      "No gold accent color found — check --color-accent")

check("No Bootstrap blue (#007bff / #0d6efd)",
      "007bff" not in html_lower and "0d6efd" not in html_lower,
      "Bootstrap default blue detected — remove it")

# Dark background
check("Dark background color present",
      bool(re.search(r'1c1c1c|161412|1e1b18|background.*#1|bg-dark|#0[0-9a-f]{5}', html_lower)),
      "No dark background color found")

# Hero section
check("Hero section exists",
      bool(re.search(r'hero|100vh|min-height.*100', html_lower)),
      "No hero section or 100vh height found")

# Before/After
check("Before/After section exists",
      bool(re.search(r'vorher|nachher|before|after|before.?after', html_lower)),
      "No Vorher/Nachher (before/after) section found")

# Navigation / footer links
check("Impressum link present",
      "impressum" in html_lower,
      "No Impressum link found")

check("Datenschutz link present",
      "datenschutz" in html_lower or "privacy" in html_lower,
      "No Datenschutz/privacy link found")

# No rounded pill buttons (border-radius > 30px is suspicious)
pill = re.search(r'border-radius\s*:\s*([5-9][0-9]|[1-9][0-9]{2,})px', html_lower)
check("No pill/rounded buttons",
      not bool(pill),
      f"Large border-radius detected: {pill.group() if pill else ''}")

# Section padding
padding_matches = re.findall(r'padding(?:-top|-bottom)?\s*:\s*(\d+)rem', html_lower)
big_padding = any(int(p) >= 4 for p in padding_matches) if padding_matches else False
check("Section padding ≥ 4rem",
      big_padding,
      f"Found padding values: {padding_matches[:5]} — needs ≥ 4rem sections")

# ── 3. Screenshot ─────────────────────────────────────────────────────────────
screenshot_ok = False
try:
    result = subprocess.run([
        "chromium-browser",
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--disable-dev-shm-usage",
        f"--screenshot={SCREENSHOT}",
        "--window-size=1280,800",
        TARGET
    ], capture_output=True, text=True, timeout=30)
    screenshot_ok = os.path.exists(SCREENSHOT) and os.path.getsize(SCREENSHOT) > 1000
    screenshot_msg = f"Saved to {SCREENSHOT}" if screenshot_ok else f"Failed: {result.stderr[:200]}"
except Exception as e:
    screenshot_msg = f"Screenshot error: {e}"

# Mobile screenshot
mobile_screenshot = SCREENSHOT.replace(".png", "-mobile.png")
try:
    subprocess.run([
        "chromium-browser",
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--disable-dev-shm-usage",
        f"--screenshot={mobile_screenshot}",
        "--window-size=375,812",
        TARGET
    ], capture_output=True, text=True, timeout=30)
except Exception:
    pass

# ── 4. Report ─────────────────────────────────────────────────────────────────
passed = [c for c in checks if c["passed"]]
failed = [c for c in checks if not c["passed"]]

print("=" * 60)
print("MENUFORGE DESIGN REVIEW")
print("=" * 60)
print(f"Target: {TARGET}")
print(f"Screenshot (desktop): {screenshot_msg}")
print(f"Screenshot (mobile):  {mobile_screenshot}")
print()
print(f"RESULT: {'✅ PASS' if not failed else '❌ FAIL'} ({len(passed)}/{len(checks)} checks passed)")
print()

if failed:
    print("FAILURES:")
    for c in failed:
        print(f"  ✗ {c['label']}")
        if c["detail"]:
            print(f"    → {c['detail']}")
    print()

if passed:
    print("PASSING:")
    for c in passed:
        print(f"  ✓ {c['label']}")

print()
print("=" * 60)

# Exit code 1 if failures
sys.exit(1 if failed else 0)
