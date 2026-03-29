#!/usr/bin/env python
import os
import sys
import django
from PIL import Image
import urllib.request

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
sys.path.insert(0, r'D:\RAMKUMAR.IN\portfolio_project')

django.setup()

from services.models import Service

print("Updating services with professional images...")

# Create media/services directory if it doesn't exist
services_dir = r'D:\RAMKUMAR.IN\portfolio_project\media\services'
os.makedirs(services_dir, exist_ok=True)

# Mapping of service slugs to image files (they will be placed by user)
services_images = {
    'data-analytics': 'data-analytics.png',      # Data Analytics image
    'digital-marketing': 'digital-marketing.png', # Digital Marketing image
    'web-development': 'web-development.png',    # Web Development image
}

print("Updating service records in database...")
services = Service.objects.all()
for service in services:
    slug = service.slug
    if slug in services_images:
        img_filename = f'services/{services_images[slug]}'
        service.image = img_filename
        service.save()
        print(f"✓ Updated: {service.title} -> {services_images[slug]}")

print(f"\n✓ Services updated successfully!")
print(f"\nNote: Place your images in: {services_dir}")
print(f"Expected filenames:")
for slug, filename in services_images.items():
    print(f"  • {filename}")
