"""
Output module for creating PDF and meta files from menu data.
"""

import os
import json
from pathlib import Path
from datetime import datetime
import weasyprint
import shutil

def create_output_files(slug: str, input_path: str, section: dict, html_content: str):
    """
    Create all output files for a menu teaser.
    
    Args:
        slug (str): Unique identifier for this menu
        input_path (str): Path to the input file
        section (dict): Section data to include in output
        html_content (str): Rendered HTML content
    """
    # Create output directory
    output_dir = Path(f"out/{slug}")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save HTML file
    html_path = output_dir / "preview.html"
    with open(html_path, 'w') as f:
        f.write(html_content)
    
    # Convert HTML to PDF  
    pdf_path = output_dir / "teaser.pdf"
    weasyprint.HTML(string=html_content).write_pdf(pdf_path)
    
    # Create meta.json
    meta = {
        'slug': slug,
        'restaurant_name': 'Example Restaurant',  # This would be determined from input
        'source_path': input_path,
        'section_name': section['name'],
        'created_at': datetime.now().isoformat(),
        'items_count': len(section['items'])
    }
    
    meta_path = output_dir / "meta.json"
    with open(meta_path, 'w') as f:
        json.dump(meta, f, indent=2)
    
    print(f"Output files created in {output_dir}")
    print(f"  - teaser.pdf")
    print(f"  - preview.html")  
    print(f"  - meta.json")

def create_before_after_pdf(original_path: str, rendered_html: str, output_dir: str):
    """
    Create a side-by-side before/after PDF (placeholder implementation).
    
    Args:
        original_path (str): Path to original menu
        rendered_html (str): Rendered HTML content
        output_dir (str): Output directory
    """
    # For now, just save the rendered HTML as the teaser
    # In a real implementation:
    # 1. Take screenshot of original menu page
    # 2. Combine with rendered HTML 
    # 3. Create PDF with side-by-side comparison
    
    print("Before/after PDF generation placeholder")
    # This would be implemented in the full version