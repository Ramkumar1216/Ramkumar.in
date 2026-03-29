#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
sys.path.insert(0, r'D:\RAMKUMAR.IN\portfolio_project')

django.setup()

from services.models import Service

print("Adding services to database...")

services_data = [
    {
        'title': 'Data Analytics',
        'slug': 'data-analytics',
        'description': 'Transform your business data into actionable insights with advanced analytics, dashboards, and reporting. I identify hidden revenue opportunities and build systems that drive measurable results.',
        'price': '₹25,000+',
        'icon': '📊',
        'features': 'Custom dashboards, Data analysis, Weekly reports, Expert consultation, Revenue impact analysis, Dashboard training',
    },
    {
        'title': 'Digital Marketing',
        'slug': 'digital-marketing',
        'description': 'Drive growth with strategic digital marketing campaigns, SEO optimization, and social media management. I focus on measurable ROI and sustainable customer acquisition.',
        'price': '₹20,000+',
        'icon': '🎯',
        'features': 'SEO optimization, Social media management, Content strategy, Campaign management, Conversion optimization, Analytics tracking',
    },
    {
        'title': 'Web Development',
        'slug': 'web-development',
        'description': 'Build responsive, modern websites with Django and React that drive conversions and engage users. I create scalable solutions that grow with your business.',
        'price': '₹35,000+',
        'icon': '💻',
        'features': 'Responsive design, SEO friendly, CMS integration, Mobile optimized, Performance optimization, Security hardening',
    },
]

# Delete existing services
Service.objects.all().delete()
print(f"Cleared existing services")

# Create services
for data in services_data:
    service = Service.objects.create(**data)
    print(f"Created: {service.title}")

print(f"\nTotal services: {Service.objects.count()}")
print("Done!")
