"""
Menu extraction module using pdfplumber and tesseract.
"""

import pdfplumber
import pytesseract
from pathlib import Path
import json
from typing import Dict, List

def extract_menu_data(input_file: str) -> Dict:
    """
    Extract menu data from a PDF or image file.
    
    Args:
        input_file (str): Path to the input file (PDF, JPG, PNG)
        
    Returns:
        Dict containing sections and their items
    """
    file_path = Path(input_file)
    file_ext = file_path.suffix.lower()
    
    if file_ext == '.pdf':
        return extract_from_pdf(input_file)
    else:
        # For images, use OCR
        return extract_from_image(input_file)

def extract_from_pdf(pdf_path: str) -> Dict:
    """
    Extract menu data from a PDF file.
    """
    sections = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            # Try to extract text and parse sections
            text = page.extract_text()
            if text:
                # Simple heuristics for section detection.
                # In a real implementation, we'd use better pattern matching.
                lines = text.split('\n')
                current_section = None
                current_items = []
                
                for line in lines:
                    line = line.strip()
                    if is_section_header(line):
                        # Save previous section if exists
                        if current_section:
                            sections.append({
                                'name': current_section,
                                'items': current_items
                            })
                        
                        # Start new section
                        current_section = line
                        current_items = []
                    elif is_menu_item(line):
                        current_items.append(parse_menu_item(line))
                
                # Save last section
                if current_section:
                    sections.append({
                        'name': current_section,
                        'items': current_items
                    })
    
    return {
        'sections': sections,
        'source': pdf_path
    }

def extract_from_image(image_path: str) -> Dict:
    """
    Extract menu data from an image file using OCR.
    """
    # Perform OCR on the image
    text = pytesseract.image_to_string(image_path)
    
    sections = []
    # Parse the OCR text similarly to PDF extraction
    # This is a simplified version - in reality, we'd need better parsing
    
    lines = text.split('\n')
    current_section = None
    current_items = []
    
    for line in lines:
        line = line.strip()
        if is_section_header(line):
            if current_section:
                sections.append({
                    'name': current_section,
                    'items': current_items
                })
            
            current_section = line
            current_items = []
        elif is_menu_item(line):
            current_items.append(parse_menu_item(line))
    
    if current_section:
        sections.append({
            'name': current_section,
            'items': current_items
        })
    
    return {
        'sections': sections,
        'source': image_path
    }

def is_section_header(line: str) -> bool:
    """
    Detect if a line is a section header.
    """
    # Common section headers (this would be more sophisticated in practice)
    headers = ['Hauptgänge', 'Vorspeisen', 'Nachtisch', 'Getränke', 'Desserts', 'Main Courses', 'Starters', 'Desserts', 'Drinks']
    return any(header in line for header in headers)

def is_menu_item(line: str) -> bool:
    """
    Detect if a line is a menu item.
    """
    # Simple heuristic: lines with a price (e.g., "2.50 CHF")
    return 'CHF' in line or 'EUR' in line or '€' in line

def parse_menu_item(line: str) -> Dict:
    """
    Parse a menu item line into name, description, price.
    """
    # This is a very basic parser - in reality, we'd use more sophisticated parsing
    parts = line.split()
    price = None
    
    # Look for price in the line
    for part in parts:
        if 'CHF' in part or 'EUR' in part or '€' in part:
            price = part
    
    # Simple text cleaning
    item_name = line.replace(price, '').strip() if price else line.strip()
    
    return {
        'name': item_name,
        'price': price,
        'description': ''  # Would be filled in real implementation
    }