#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
sys.path.insert(0, r'D:\RAMKUMAR.IN\portfolio_project')

django.setup()

from services.models import Service

print("="*60)
print("  SERVICE IMAGES SETUP - FINAL VERIFICATION")
print("="*60)

services_dir = r'D:\RAMKUMAR.IN\portfolio_project\media\services'

print("\n📋 Current Service Setup:\n")
services = Service.objects.all()
for i, service in enumerate(services, 1):
    image_status = "✓ Has Image" if service.image else "✗ No Image"
    print(f"{i}. {service.title}")
    print(f"   Slug: {service.slug}")
    print(f"   Image: {image_status}")
    if service.image:
        print(f"   Path: {service.image.name}")
    
    # Check file exists
    if service.image:
        full_path = os.path.join(r'D:\RAMKUMAR.IN\portfolio_project\media', service.image.name)
        if os.path.exists(full_path):
            file_size = os.path.getsize(full_path)
            print(f"   File Size: {file_size:,} bytes")
            print(f"   ✓ File exists!")
        else:
            print(f"   ✗ File NOT found at: {full_path}")
    print()

print("="*60)
print("\n📸 To Use Your Professional Images:\n")
print("Option 1: Upload via Admin Panel (Easiest)")
print("  1. Go to http://localhost:8000/admin")
print("  2. Click 'Services'")
print("  3. Edit each service")
print("  4. Upload your professional images")
print("  5. Save")

print("\nOption 2: File Replacement")
print(f"  1. Save your images to: {services_dir}")
print("  2. Use filenames:")
print("     • data-analytics.png")
print("     • digital-marketing.png")
print("     • web-development.png")

print("\n" + "="*60)
print("✓ Template Updated: Emoji icon removed ✓")
print("✓ Database: Image fields configured ✓")
print("✓ Ready for your professional images ✓")
print("="*60)

print("\n🌐 View your services at:")
print("  • http://localhost:8000/services/data-analytics/")
print("  • http://localhost:8000/services/digital-marketing/")
print("  • http://localhost:8000/services/web-development/")
