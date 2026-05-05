#!/usr/bin/env python3
"""
Create a simple PDF menu for testing the pipeline
"""
import os
from fpdf import FPDF

# Create a simple PDF menu
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add some sample menu data
menu_content = [
    "Sample Restaurant Menu",
    "",
    "Hauptgerichte",
    "",
    "Steak au Poivre",
    "Rindfleisch, Pfeffer-Sauce, Gemüse, Kartoffeln",
    "CHF 24.50",
    "",
    "Wildschwein-Schnitzel",
    "Schwein, Senf-Sauce, Gemüse, Reis",
    "CHF 22.00",
    "",
    "Geflügel-Curry",
    "Hühnchen, Curry-Sauce, Gemüse, Reis",
    "CHF 19.50",
    "",
    "Desserts",
    "",
    "Tiramisu",
    "Eier, Kaffee, Schokolade",
    "CHF 8.00",
    "",
    "Apfelstreusel",
    "Apfel, Zimt, Sauerteig",
    "CHF 7.50"
]

for line in menu_content:
    pdf.cell(0, 10, line, ln=True)

# Save the PDF
pdf.output("/home/bloxperts/menuforge/test_menus/sample_menu.pdf")
print("Sample menu PDF created successfully.")