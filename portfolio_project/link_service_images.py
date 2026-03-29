#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
sys.path.insert(0, r'D:\RAMKUMAR.IN\portfolio_project')

django.setup()

from services.models import Service

print("Linking images to services...")

# Service to image mapping
image_mapping = {
    'data-analytics': 'services/data-analytics.jpg',
    'digital-marketing': 'services/digital-marketing.jpg',
    'web-development': 'services/web-development.jpg',
}

for slug, image_path in image_mapping.items():
    try:
        service = Service.objects.get(slug=slug)
        service.image = image_path
        service.save()
        print(f"✓ Updated {service.title} with image: {image_path}")
    except Service.DoesNotExist:
        print(f"✗ Service with slug '{slug}' not found")

print("\nDone! All services should now display images.")
print(f"Total services: {Service.objects.count()}")

# Verify
for service in Service.objects.all():
    if service.image:
        print(f"  {service.title}: {service.image.url}")
    else:
        print(f"  {service.title}: NO IMAGE")
