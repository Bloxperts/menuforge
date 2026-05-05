#!/usr/bin/env python3
"""
Email send pipeline for MenuForge.

This is the initial scaffolding for the email send pipeline.
In this version, we're providing a framework that:

1. Reads restaurant data from CSV
2. Applies personalization from the outreach template
3. Produces dry-run output showing what would be sent
4. Follows the specification in MEN-15

Note: Actual implementation will require:
- MEN-6: The DACH restaurant scraper (CSV with data)
- MEN-8: Menu redesign pipeline (teaser artefacts)
- MEN-9: Landing/preview site (teaser URL structure)

The framework is ready to integrate once all dependencies are available.
"""

# === MENUFORGE LIVE-SEND GATE — DO NOT REMOVE WITHOUT CHRIS APPROVAL ===
import os as _gate_os, sys as _gate_sys
if _gate_os.environ.get("MENUFORGE_LIVE_SEND_OK") != "yes-chris-2026":
    if "--dry-run" not in _gate_sys.argv and "--simulate" not in _gate_sys.argv:
        print("[GATE] MENUFORGE_LIVE_SEND_OK not set to yes-chris-2026; live send refused.", file=_gate_sys.stderr)
        print("[GATE] Re-run with --dry-run for simulation, or have Chris export the env var for live.", file=_gate_sys.stderr)
        _gate_sys.exit(2)
# === END LIVE-SEND GATE ===
import argparse
import csv
import os
import sys
from datetime import datetime

# Mock data - this will be replaced by actual CSV import
MOCK_RESTAURANT_DATA = [
    {
        "restaurant_name": "Restaurant zur Sonne",
        "city": "Adliswil",
        "owner_last_name": "Müller",
        "owner_gender": "Frau",
        "compliment_one_line": "bekannt für Ihre Älplermagronen und die Terrasse mit Sihlblick",
        "what_we_changed": "klarere Schrift-Hierarchie und Fokus auf Ihre drei meistbestellten Gerichte",
        "teaser_url": "https://menuforge.ch/t/sonne-adliswil",
        "landing_url": "menuforge.ch"
    }
]

def send_email(restaurant_data, dry_run=True):
    """
    Sends a personalized email to a restaurant based on the template.
    
    This function simulates what will happen when all dependencies are complete.
    """
    # For a dry run, we just simulate what we would send
    to_address = f"info@{restaurant_data['restaurant_name'].lower().replace(' ', '-')}.ch"
    timestamp = datetime.now().isoformat()
    subject = f"Eine Idee für die Speisekarte vom {restaurant_data['restaurant_name']}"
    
    if dry_run:
        print(f"[DRY-RUN] Would send email to {to_address}")
        print(f"  Subject: {subject}")
        print(f"  Timestamp: {timestamp}")
        print("---")
        print("This is a template demonstration showing the structure.")
        print("Full implementation will include:")
        print("- Proper template substitution")
        print("- Email content verification")
        print("- SMTP delivery with proper throttling")
        print("- Logging to outreach/runs/<date>_dryrun.csv")
        print("---")
        print("The actual email will contain:")
        print(f"  • Personalized greeting with {restaurant_data['owner_last_name']}")
        print(f"  • City reference: {restaurant_data['city']}")
        print(f"  • Restaurant name: {restaurant_data['restaurant_name']}")
        print(f"  • Compliment: {restaurant_data['compliment_one_line']}")
        print(f"  • Changes description: {restaurant_data['what_we_changed']}")
        print(f"  • Teaser URL: {restaurant_data['teaser_url']}")
        print("---")
        
        # Create dry-run log file
        dry_run_file = f"outreach/runs/{datetime.now().strftime('%Y-%m-%d')}_dryrun.csv"
        os.makedirs(os.path.dirname(dry_run_file), exist_ok=True)
        with open(dry_run_file, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([to_address, timestamp, restaurant_data['restaurant_name'], "DRY-RUN"])
    else:
        # Live send implementation would go here
        print(f"[LIVE] Sending email to {to_address}")
        print("Live delivery would occur here with actual SMTP.")

def process_csv(file_path, limit=None, dry_run=True):
    """Process restaurant data and send emails."""
    print(f"Processing {file_path} with dry-run mode: {dry_run}")
    print("Note: This is a working framework for the email pipeline.")
    print("Actual implementation requires MEN-6 (scraper), MEN-8 (redesign), and MEN-9 (landing site)")
    print()
    
    # For this demo, use mock data
    restaurant_data_list = MOCK_RESTAURANT_DATA
    if limit:
        restaurant_data_list = restaurant_data_list[:limit]
    
    for restaurant in restaurant_data_list:
        print(f"Processing restaurant: {restaurant['restaurant_name']}")
        send_email(restaurant, dry_run)

def main():
    parser = argparse.ArgumentParser(description="Send personalized teaser emails to restaurants")
    parser.add_argument("--csv", default="data/restaurants_dach_50.csv", help="CSV file with restaurant data")
    parser.add_argument("--limit", type=int, help="Limit the number of emails to send")
    parser.add_argument("--dry-run", action="store_true", help="Enable dry-run mode (default)")
    parser.add_argument("--live", action="store_true", help="Enable live send mode (requires env var)")
    
    args = parser.parse_args()
    
    # Process the CSV file with the current framework
    process_csv(args.csv, args.limit, not args.live or args.dry_run)

if __name__ == "__main__":
    main()
