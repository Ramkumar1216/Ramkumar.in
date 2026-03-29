#!/usr/bin/env python
import os
import sys
import django
from PIL import Image, ImageDraw, ImageFont

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
sys.path.insert(0, r'D:\RAMKUMAR.IN\portfolio_project')

django.setup()

from services.models import Service

print("Creating professional service images...")

# Create media/services directory if it doesn't exist
services_dir = r'D:\RAMKUMAR.IN\portfolio_project\media\services'
os.makedirs(services_dir, exist_ok=True)

# Image specifications
img_width, img_height = 800, 500

# Service configurations with better designs
services_config = {
    'data-analytics': {
        'title': 'Data Analytics',
        'emoji': '📊',
        'bg_color': (20, 33, 61),  # Dark blue
        'accent_color': (0, 150, 255),  # Bright blue
        'description': 'Transform Data into Insights'
    },
    'digital-marketing': {
        'title': 'Digital Marketing',
        'emoji': '🎯',
        'bg_color': (40, 20, 60),  # Dark purple
        'accent_color': (255, 100, 200),  # Pink
        'description': 'Drive Growth & Engagement'
    },
    'web-development': {
        'title': 'Web Development',
        'emoji': '💻',
        'bg_color': (10, 40, 30),  # Dark teal
        'accent_color': (0, 200, 150),  # Bright teal
        'description': 'Build Modern Websites'
    }
}

for slug, config in services_config.items():
    print(f"\nCreating image for {config['title']}...")
    
    # Create image with gradient background simulation
    img = Image.new('RGB', (img_width, img_height), color=config['bg_color'])
    draw = ImageDraw.Draw(img)
    
    # Draw accent bar at top
    bar_height = 10
    draw.rectangle([(0, 0), (img_width, bar_height)], fill=config['accent_color'])
    
    # Draw large emoji
    emoji_size = 120
    emoji_text = config['emoji']
    
    # Add large emoji in upper area
    try:
        emoji_font = ImageFont.load_default()
    except:
        emoji_font = ImageFont.load_default()
    
    # Position emoji
    emoji_bbox = draw.textbbox((0, 0), emoji_text, font=emoji_font)
    emoji_width = emoji_bbox[2] - emoji_bbox[0]
    emoji_x = (img_width - emoji_width) // 2
    emoji_y = 60
    
    draw.text((emoji_x, emoji_y), emoji_text, fill=config['accent_color'], font=emoji_font)
    
    # Add service title
    title_text = config['title']
    title_bbox = draw.textbbox((0, 0), title_text, font=emoji_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (img_width - title_width) // 2
    title_y = 220
    
    draw.text((title_x, title_y), title_text, fill=(255, 255, 255), font=emoji_font)
    
    # Add description
    desc_text = config['description']
    desc_bbox = draw.textbbox((0, 0), desc_text, font=emoji_font)
    desc_width = desc_bbox[2] - desc_bbox[0]
    desc_x = (img_width - desc_width) // 2
    desc_y = 300
    
    draw.text((desc_x, desc_y), desc_text, fill=config['accent_color'], font=emoji_font)
    
    # Add decorative elements
    # Bottom accent bar
    draw.rectangle([(0, img_height - 10), (img_width, img_height)], fill=config['accent_color'])
    
    # Save image
    img_path = os.path.join(services_dir, f'{slug}.png')
    img.save(img_path)
    print(f"✓ Created: {slug}.png ({img_width}x{img_height})")

print("\n" + "="*50)
print("Updating services with professional images...")
print("="*50)

# Update services with images
services = Service.objects.all()
for service in services:
    img_filename = f'services/{service.slug}.png'
    if service.image != img_filename:
        service.image = img_filename
        service.save()
        print(f"✓ Updated: {service.title}")
    else:
        print(f"✓ Already set: {service.title}")

total = services.count()
print(f"\n{'='*50}")
print(f"✓ SUCCESS! Created {total} professional service images!")
print(f"{'='*50}")
print(f"\nImages are now visible on service detail pages:")
print(f"  • http://localhost:8000/services/data-analytics/")
print(f"  • http://localhost:8000/services/digital-marketing/")
print(f"  • http://localhost:8000/services/web-development/")
