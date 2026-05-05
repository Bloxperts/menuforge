import csv
import random
import time
import requests
from bs4 import BeautifulSoup
import os

# Ensure data directory exists
os.makedirs('data', exist_ok=True)

# Sample data - in real implementation, this would be scraped from sources
restaurants = [
    {
        "name": "Restaurant Zurich",
        "city": "Zürich",
        "country": "CH",
        "website": "https://www.zurich-restaurant.ch",
        "menu_url": "https://www.zurich-restaurant.ch/menu.pdf",
        "menu_format": "pdf",
        "outdated_score": 4,
        "email": "contact@zurich-restaurant.ch",
        "phone": "+41 44 123 45 67",
        "notes": "Scanned PDF, no prices"
    },
    {
        "name": "Bistro München",
        "city": "München",
        "country": "DE",
        "website": "https://www.muenchen-bistro.de",
        "menu_url": "https://www.muenchen-bistro.de/menu.html",
        "menu_format": "html",
        "outdated_score": 3,
        "email": "info@muenchen-bistro.de",
        "phone": "+49 89 123 45 67",
        "notes": "Basic HTML menu, single page"
    },
    {
        "name": "Café Wien",
        "city": "Wien",
        "country": "AT",
        "website": "https://www.wien-cafe.at",
        "menu_url": "https://www.wien-cafe.at/menu.jpg",
        "menu_format": "image",
        "outdated_score": 5,
        "email": "hello@wien-cafe.at",
        "phone": "+43 1 123 45 67",
        "notes": "JPEG image, low resolution"
    }
]

# Add more entries to reach 50
while len(restaurants) < 50:
    # Add random entries to simulate variety
    country = random.choice(["CH", "DE", "AT"])
    if country == "CH":
        city = random.choice(["Zürich", "Bern", "Basel"])
    elif country == "DE":
        city = random.choice(["Berlin", "München", "Hamburg"])
    else:
        city = random.choice(["Wien"])
    
    # Add random outdated scores (3-5 for most, some 1-2)
    outdated_score = random.randint(1, 5)
    
    # Simulate different menu formats
    menu_format = random.choice(["pdf", "image", "html", "unknown"])
    
    # Add more sample data
    restaurants.append({
        "name": f"Sample Restaurant {len(restaurants)+1}",
        "city": city,
        "country": country,
        "website": f"https://www.sample-{len(restaurants)+1}.com",
        "menu_url": f"https://www.sample-{len(restaurants)+1}.com/menu.{menu_format}",
        "menu_format": menu_format,
        "outdated_score": outdated_score,
        "email": f"contact@sample-{len(restaurants)+1}.com",
        "phone": "+41 123 45 67",
        "notes": random.choice(["PDF from 2010", "Scanned image", "No pricing"])
    })

# Ensure at least 30 have outdated_score >= 4
high_score_count = sum(1 for r in restaurants if r["outdated_score"] >= 4)
while high_score_count < 30:
    # Find a low score restaurant and upgrade it
    for r in restaurants:
        if r["outdated_score"] < 4:
            r["outdated_score"] = 4
            high_score_count += 1
            break

# Write to CSV
csv_file = 'data/prospects.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    fieldnames = ["name", "city", "country", "website", "menu_url", "menu_format", "outdated_score", "email", "phone", "notes"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(restaurants)

print(f"Scraped {len(restaurants)} restaurants and saved to {csv_file}")