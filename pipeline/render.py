"""
Menu rendering module for creating teasers.
"""

from jinja2 import Template
import os
from pathlib import Path

# HTML template for the teaser
TEASER_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ section_name }} - MenuForge Teaser</title>
    <style>
        body {
            font-family: 'DM Sans', sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #161412;
            color: #F0EBE3;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #1E1B18;
            padding: 30px;
            border: 1px solid #2E2A25;
            border-radius: 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .section-title {
            font-family: 'Cormorant Garamond', serif;
            font-size: 24px;
            font-weight: 600;
            color: #C4973A;
            border-bottom: 2px solid #2E2A25;
            padding-bottom: 10px;
            margin-bottom: 25px;
        }
        .menu-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 0;
            border-bottom: 1px solid #2E2A25;
        }
        .menu-item:last-child {
            border-bottom: none;
        }
        .item-name {
            font-family: 'DM Sans', sans-serif;
            font-size: 16px;
            font-weight: 500;
            color: #F0EBE3;
        }
        .item-description {
            font-family: 'DM Sans', sans-serif;
            font-size: 14px;
            color: #8C8279;
            font-style: italic;
        }
        .item-price {
            font-family: 'DM Sans', sans-serif;
            font-size: 16px;
            font-weight: 700;
            color: #C4973A;
        }
        .footer {
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #2E2A25;
            text-align: center;
            font-size: 12px;
            color: #8C8279;
        }
        .footer a {
            color: #C4973A;
            text-decoration: none;
        }
        <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">

<body>
    <div class="container">
        <div class="section-title">{{ section_name }}</div>
        {% for item in items %}
        <div class="menu-item">
            <div>
                <div class="item-name">{{ item.name }}</div>
                <div class="item-description">{{ item.description }}</div>
            </div>
            <div class="item-price">{{ item.price }}</div>
        </div>
        {% endfor %}
        <div class="footer">
            Created with <a href="https://menuforge.ch">MenuForge</a> - Transforming restaurant menus
        </div>
    </div>
</body>
</html>
"""

def render_section(section: dict) -> str:
    """
    Render a menu section into HTML using the teaser template.
    
    Args:
        section (dict): Section data including name and items
        
    Returns:
        str: Rendered HTML string
    """
    template = Template(TEASER_TEMPLATE)
    
    # Render the HTML
    html = template.render(
        section_name=section['name'],
        items=section['items']
    )
    
    return html

def save_html(html_content: str, output_path: str):
    """
    Save the rendered HTML to a file.
    
    Args:
        html_content (str): HTML content to save
        output_path (str): Path to save the HTML file
    """
    with open(output_path, 'w') as f:
        f.write(html_content)
        
    print(f"Saved HTML to {output_path}")