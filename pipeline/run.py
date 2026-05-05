#!/usr/bin/env python3
"""
MenuForge pipeline runner for processing restaurant menus into teasers.

Usage:
  python pipeline/run.py --input <path> --slug <name>
"""

import argparse
import os
import sys
from pathlib import Path

# Add the pipeline directory to the path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent))

from pipeline.extract import extract_menu_data
from pipeline.render import render_section
from pipeline.output import create_output_files

def main():
    parser = argparse.ArgumentParser(description="MenuForge pipeline")
    parser.add_argument('--input', required=True, help='Input file (PDF, JPG, PNG)')
    parser.add_argument('--slug', required=True, help='Output slug for this menu')
    
    args = parser.parse_args()
    
    # Create output directory
    output_dir = Path(f"out/{args.slug}")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Step 1: Extract menu data
    print(f"Extracting data from {args.input}...")
    menu_data = extract_menu_data(args.input)
    
    # Step 2: Choose the section with the most items
    print("Choosing section to showcase...")
    section = max(menu_data['sections'], key=lambda s: len(s['items']))
    
    # Step 3: Render the teaser
    print("Rendering teaser...")
    rendered_html = render_section(section)
    
    # Step 4: Create output files
    print("Creating output files...")
    create_output_files(args.slug, args.input, section, rendered_html)
    
    print(f"Pipeline complete. Outputs in {output_dir}")

if __name__ == "__main__":
    main()