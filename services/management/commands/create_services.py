from django.core.management.base import BaseCommand
from services.models import Service

class Command(BaseCommand):
    help = 'Create default services if they do not exist'

    def handle(self, *args, **options):
        services = [
            {
                'title': 'Data Analytics',
                'slug': 'data-analytics',
                'description': 'Transform your business data into actionable insights with advanced analytics, dashboards, and reporting.',
                'price': '₹25,000+',
                'icon': '📊',
                'features': 'Custom dashboards, Data analysis, Weekly reports, Expert consultation, Revenue impact analysis, Dashboard training',
            },
            {
                'title': 'Digital Marketing',
                'slug': 'digital-marketing',
                'description': 'Drive growth with strategic digital marketing campaigns, SEO optimization, and social media management.',
                'price': '₹20,000+',
                'icon': '🎯',
                'features': 'SEO optimization, Social media management, Content strategy, Campaign management, Conversion optimization, Analytics tracking',
            },
            {
                'title': 'Web Development',
                'slug': 'web-development',
                'description': 'Build responsive, modern websites with Django and React that drive conversions and engage users.',
                'price': '₹35,000+',
                'icon': '💻',
                'features': 'Responsive design, SEO friendly, CMS integration, Mobile optimized, Performance optimization, Security hardening',
            },
        ]
        
        for service_data in services:
            service, created = Service.objects.update_or_create(
                slug=service_data['slug'],
                defaults=service_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Created service: {service.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'↻ Updated service: {service.title}'))
