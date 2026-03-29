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
from django.core.files.base import ContentFile
from io import BytesIO

print("Creating service images...")

# Create media/services directory if it doesn't exist
services_dir = r'D:\RAMKUMAR.IN\portfolio_project\media\services'
os.makedirs(services_dir, exist_ok=True)

# Image specifications
img_width, img_height = 600, 400
colors = {
    'data-analytics': (30, 58, 138),  # Dark blue
    'digital-marketing': (139, 0, 139),  # Dark magenta
    'web-development': (0, 100, 0),  # Dark green
}

icons = {
    'data-analytics': '📊',
    'digital-marketing': '🎯',
    'web-development': '💻',
}

services_data = {
    'data-analytics': ('Data Analytics', '📊 Data Analytics'),
    'digital-marketing': ('Digital Marketing', '🎯 Digital Marketing'),
    'web-development': ('Web Development', '💻 Web Development'),
}

for slug, (title, display_text) in services_data.items():
    # Create a colorful image
    color = colors[slug]
    img = Image.new('RGB', (img_width, img_height), color=color)
    draw = ImageDraw.Draw(img)
    
    # Add gradient effect with text
    try:
        # Try to use a larger font if available
        font = ImageFont.load_default()
    except:
        font = ImageFont.load_default()
    
    # Add text to image
    text = display_text
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Center the text
    x = (img_width - text_width) // 2
    y = (img_height - text_height) // 2
    
    draw.text((x, y), text, fill=(255, 255, 255), font=font)
    
    # Save image
    img_path = os.path.join(services_dir, f'{slug}.png')
    img.save(img_path)
    print(f"✓ Created image: {slug}.png")

# Update services with images
print("\nUpdating services with images...")

services = Service.objects.all()
for service in services:
    img_filename = f'services/{service.slug}.png'
    service.image = img_filename
    service.save()
    print(f"✓ Updated: {service.title}")

print(f"\n✓ All {services.count()} services now have images!")
