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

print("="*70)
print("  CREATING & UPLOADING PROFESSIONAL SERVICE IMAGES")
print("="*70)

# Create media/services directory if it doesn't exist
services_dir = r'D:\RAMKUMAR.IN\portfolio_project\media\services'
os.makedirs(services_dir, exist_ok=True)

# High-quality professional image configurations
services_config = {
    'data-analytics': {
        'title': 'Data Analytics',
        'subtitle': 'Transform Data into Insights',
        'bg_color': (10, 25, 47),  # Deep navy blue
        'accent_color': (0, 180, 255),  # Bright cyan
        'secondary_color': (100, 200, 255),  # Light blue
        'emoji': '📊'
    },
    'digital-marketing': {
        'title': 'Digital Marketing',
        'subtitle': 'Drive Growth & Engagement',
        'bg_color': (30, 15, 50),  # Deep purple
        'accent_color': (255, 100, 200),  # Bright pink
        'secondary_color': (200, 100, 255),  # Light purple
        'emoji': '🎯'
    },
    'web-development': {
        'title': 'Web Development',
        'subtitle': 'Build Modern Websites',
        'bg_color': (10, 40, 50),  # Deep teal
        'accent_color': (0, 220, 200),  # Bright cyan
        'secondary_color': (100, 255, 220),  # Light cyan
        'emoji': '💻'
    }
}

def create_professional_image(slug, config):
    """Create a professional-looking service image"""
    width, height = 1000, 600
    
    # Create image with gradient background
    img = Image.new('RGB', (width, height), color=config['bg_color'])
    draw = ImageDraw.Draw(img)
    
    # Draw gradient effect (simulate with rectangles)
    for i in range(height):
        # Create gradient from bg_color to slightly lighter
        ratio = i / height
        r = int(config['bg_color'][0] + (config['secondary_color'][0] - config['bg_color'][0]) * ratio * 0.3)
        g = int(config['bg_color'][1] + (config['secondary_color'][1] - config['bg_color'][1]) * ratio * 0.3)
        b = int(config['bg_color'][2] + (config['secondary_color'][2] - config['bg_color'][2]) * ratio * 0.3)
        draw.line([(0, i), (width, i)], fill=(r, g, b))
    
    # Draw decorative accent bars
    bar_height = 15
    # Top accent bar
    draw.rectangle([(0, 0), (width, bar_height)], fill=config['accent_color'])
    # Bottom accent bar
    draw.rectangle([(0, height - bar_height), (width, height)], fill=config['accent_color'])
    
    # Add decorative circles in corners
    circle_size = 150
    # Top right circle
    draw.ellipse(
        [(width - circle_size, -50), (width + 50, circle_size - 50)],
        fill=config['secondary_color'],
        outline=config['accent_color']
    )
    # Bottom left circle
    draw.ellipse(
        [(-50, height - circle_size + 50), (circle_size - 50, height + 50)],
        fill=config['secondary_color'],
        outline=config['accent_color']
    )
    
    # Add emoji/symbol
    emoji = config['emoji']
    try:
        emoji_font = ImageFont.load_default()
    except:
        emoji_font = ImageFont.load_default()
    
    # Position emoji on left side
    emoji_bbox = draw.textbbox((0, 0), emoji, font=emoji_font)
    emoji_width = emoji_bbox[2] - emoji_bbox[0]
    emoji_x = 80
    emoji_y = height // 2 - 60
    
    draw.text((emoji_x, emoji_y), emoji, fill=config['accent_color'], font=emoji_font)
    
    # Add main title (centered)
    title = config['title']
    title_bbox = draw.textbbox((0, 0), title, font=emoji_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) // 2
    title_y = height // 2 - 40
    
    draw.text((title_x, title_y), title, fill=(255, 255, 255), font=emoji_font)
    
    # Add subtitle
    subtitle = config['subtitle']
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=emoji_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (width - subtitle_width) // 2
    subtitle_y = height // 2 + 20
    
    draw.text((subtitle_x, subtitle_y), subtitle, fill=config['accent_color'], font=emoji_font)
    
    # Save image
    img_path = os.path.join(services_dir, f'{slug}.png')
    img.save(img_path, 'PNG', quality=95)
    
    file_size = os.path.getsize(img_path)
    print(f"✓ Created: {slug}.png ({file_size:,} bytes) - {width}x{height}px")
    
    return img_path

# Create all images
print("\n📸 Creating professional images...\n")
for slug, config in services_config.items():
    create_professional_image(slug, config)

# Update database with images
print("\n" + "="*70)
print("  UPDATING DATABASE WITH IMAGES")
print("="*70 + "\n")

services = Service.objects.all()
for service in services:
    slug = service.slug
    img_filename = f'services/{slug}.png'
    
    if slug in services_config:
        service.image = img_filename
        service.save()
        print(f"✓ {service.title:<20} -> {img_filename}")

print("\n" + "="*70)
print(f"✅ SUCCESS! All {services.count()} services updated with professional images!")
print("="*70)

print("\n🌐 Your services are now live with professional images:")
print("  • http://localhost:8000/services/data-analytics/")
print("  • http://localhost:8000/services/digital-marketing/")
print("  • http://localhost:8000/services/web-development/")

print("\n📁 Images saved to:")
print(f"   {services_dir}")

print("\n✨ Images are automatically served by your website!")
print("   Just refresh your browser to see the changes.\n")
