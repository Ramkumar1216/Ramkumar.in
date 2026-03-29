#!/usr/bin/env python
"""
Django shell management script for common tasks
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from django.core.management import call_command

def create_sample_data():
    """Create sample data for testing"""
    from services.models import Service
    from projects.models import Project
    from core.models import Testimonial
    
    # Create sample services
    services_data = [
        {
            'title': 'Data Analytics',
            'slug': 'data-analytics',
            'description': 'Transform your business data into actionable insights with advanced analytics, dashboards, and reporting.',
            'price': '₹999+',
            'icon': '📊',
            'features': 'Custom dashboards, Data analysis, Weekly reports, Expert consultation',
        },
        {
            'title': 'Digital Marketing',
            'slug': 'digital-marketing',
            'description': 'Drive growth with strategic digital marketing campaigns, SEO optimization, and social media management.',
            'price': '₹1499+',
            'icon': '🎯',
            'features': 'SEO optimization, Social media management, Content strategy, Campaign management',
        },
        {
            'title': 'Web Development',
            'slug': 'web-development',
            'description': 'Build responsive, modern websites with Django and React that drive conversions and engage users.',
            'price': '₹1999+',
            'icon': '💻',
            'features': 'Responsive design, SEO friendly, CMS integration, Mobile optimized',
        },
    ]
    
    for service_data in services_data:
        Service.objects.get_or_create(slug=service_data['slug'], defaults=service_data)
    
    # Create sample testimonials
    testimonials_data = [
        {
            'name': 'Arun Kumar',
            'feedback': 'Ramkumar helped us increase our online sales by 150% in just 3 months. Highly recommended!',
            'rating': 5,
        },
        {
            'name': 'Priya Sharma',
            'feedback': 'Professional, knowledgeable, and results-driven. Best decision we made for our business.',
            'rating': 5,
        },
        {
            'name': 'Vikram Singh',
            'feedback': 'Great communication and delivers exactly what was promised. Would work with him again!',
            'rating': 5,
        },
    ]
    
    for testimonial_data in testimonials_data:
        Testimonial.objects.get_or_create(name=testimonial_data['name'], defaults=testimonial_data)
    
    print("✓ Sample data created successfully!")
    print("  - 3 Services")
    print("  - 3 Testimonials")

if __name__ == '__main__':
    create_sample_data()
