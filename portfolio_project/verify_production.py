#!/usr/bin/env python
"""
Production Deployment Verification Script
Checks if your Django project is ready for production deployment
"""

import os
import sys
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
BASE_DIR = Path(__file__).resolve().parent

sys.path.insert(0, str(BASE_DIR))
django.setup()

from django.core.management import call_command
from django.conf import settings
from services.models import Service


class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'


def print_header(text):
    print(f"\n{Colors.BLUE}{'='*60}")
    print(f"{text.center(60)}")
    print(f"{'='*60}{Colors.END}\n")


def check_passed(msg):
    print(f"{Colors.GREEN}✓ {msg}{Colors.END}")


def check_failed(msg):
    print(f"{Colors.RED}✗ {msg}{Colors.END}")


def check_warning(msg):
    print(f"{Colors.YELLOW}⚠ {msg}{Colors.END}")


def verify_environment():
    """Check environment configuration"""
    print_header("ENVIRONMENT CONFIGURATION")
    
    checks = []
    
    # Check DEBUG
    if not settings.DEBUG:
        check_passed("DEBUG = False (Production mode)")
        checks.append(True)
    else:
        check_failed("DEBUG = True (Should be False in production)")
        checks.append(False)
    
    # Check SECRET_KEY
    if settings.SECRET_KEY and 'insecure' not in settings.SECRET_KEY.lower():
        check_passed("SECRET_KEY is set and not the default")
        checks.append(True)
    else:
        check_failed("SECRET_KEY is insecure or default - please change it")
        checks.append(False)
    
    # Check ALLOWED_HOSTS
    if '*' not in settings.ALLOWED_HOSTS:
        check_passed(f"ALLOWED_HOSTS properly configured: {settings.ALLOWED_HOSTS}")
        checks.append(True)
    else:
        check_warning("ALLOWED_HOSTS contains '*' - should specify exact domains")
        checks.append(False)
    
    # Check environment variable
    env = os.environ.get('ENVIRONMENT', 'development')
    if env == 'production':
        check_passed("ENVIRONMENT = production")
        checks.append(True)
    else:
        check_warning(f"ENVIRONMENT = {env} (set to 'production' if going live)")
        checks.append(False)
    
    return sum(checks) / len(checks) * 100


def verify_security():
    """Check security settings"""
    print_header("SECURITY SETTINGS")
    
    checks = []
    
    # HTTPS settings
    if not settings.DEBUG:
        if getattr(settings, 'SECURE_SSL_REDIRECT', False):
            check_passed("SECURE_SSL_REDIRECT enabled (HTTPS required)")
            checks.append(True)
        else:
            check_warning("SECURE_SSL_REDIRECT disabled")
            checks.append(False)
        
        if getattr(settings, 'SESSION_COOKIE_SECURE', False):
            check_passed("SESSION_COOKIE_SECURE enabled")
            checks.append(True)
        else:
            check_warning("SESSION_COOKIE_SECURE disabled")
            checks.append(False)
        
        if getattr(settings, 'CSRF_COOKIE_SECURE', False):
            check_passed("CSRF_COOKIE_SECURE enabled")
            checks.append(True)
        else:
            check_warning("CSRF_COOKIE_SECURE disabled")
            checks.append(False)
    else:
        check_warning("DEBUG=True; Security settings not checked (enable in production)")
    
    # Check XSS Protection
    if getattr(settings, 'SECURE_BROWSER_XSS_FILTER', False):
        check_passed("XSS filtering enabled")
        checks.append(True)
    else:
        check_warning("XSS filtering could be stronger")
        checks.append(False)
    
    # Password validators
    if len(settings.AUTH_PASSWORD_VALIDATORS) > 0:
        check_passed(f"Password validation enabled ({len(settings.AUTH_PASSWORD_VALIDATORS)} validators)")
        checks.append(True)
    else:
        check_failed("No password validators configured")
        checks.append(False)
    
    return sum(checks) / max(len(checks), 1) * 100


def verify_database():
    """Check database configuration"""
    print_header("DATABASE CONFIGURATION")
    
    checks = []
    
    # Database engine
    db_engine = settings.DATABASES['default']['ENGINE']
    if 'postgresql' in db_engine:
        check_passed("Using PostgreSQL (production-ready)")
        checks.append(True)
    elif 'sqlite' in db_engine:
        if settings.DEBUG:
            check_passed("Using SQLite (acceptable for development)")
            checks.append(True)
        else:
            check_warning("Using SQLite in production (consider PostgreSQL)")
            checks.append(False)
    else:
        check_passed(f"Using {db_engine}")
        checks.append(True)
    
    # Database connection
    try:
        from django.db import connection
        connection.ensure_connection()
        check_passed("Database connection successful")
        checks.append(True)
    except Exception as e:
        check_failed(f"Database connection failed: {str(e)}")
        checks.append(False)
    
    # Migrations
    from django.core.management import call_command
    try:
        call_command('migrate', '--check', '--dry-run', verbosity=0)
        check_passed("All migrations applied")
        checks.append(True)
    except Exception:
        check_failed("Pending migrations exist - run 'python manage.py migrate'")
        checks.append(False)
    
    return sum(checks) / len(checks) * 100


def verify_static_files():
    """Check static files configuration"""
    print_header("STATIC FILES CONFIGURATION")
    
    checks = []
    
    # Static URL
    if settings.STATIC_URL:
        check_passed(f"STATIC_URL configured: {settings.STATIC_URL}")
        checks.append(True)
    else:
        check_failed("STATIC_URL not configured")
        checks.append(False)
    
    # Static root
    if settings.STATIC_ROOT:
        check_passed(f"STATIC_ROOT configured: {settings.STATIC_ROOT}")
        checks.append(True)
    else:
        check_failed("STATIC_ROOT not configured")
        checks.append(False)
    
    # Whitenoise
    from django.conf import settings
    static_storage = getattr(settings, 'STATICFILES_STORAGE', '')
    if 'whitenoise' in static_storage.lower():
        check_passed("Whitenoise compression enabled")
        checks.append(True)
    else:
        check_warning("Whitenoise not enabled - consider enabling for better performance")
        checks.append(False)
    
    return sum(checks) / len(checks) * 100


def verify_data():
    """Check if required data exists"""
    print_header("DATA & CONTENT")
    
    checks = []
    
    # Services
    try:
        services_count = Service.objects.count()
        if services_count >= 3:
            check_passed(f"Services configured ({services_count} services found)")
            checks.append(True)
        else:
            check_failed(f"Not enough services ({services_count} found, need at least 3)")
            check_warning("Run: python manage.py create_default_services")
            checks.append(False)
    except Exception as e:
        check_failed(f"Error checking services: {str(e)}")
        checks.append(False)
    
    # Check specific services
    required_slugs = ['data-analytics', 'digital-marketing', 'web-development']
    for slug in required_slugs:
        try:
            service = Service.objects.get(slug=slug)
            check_passed(f"✓ Service found: {service.title}")
            checks.append(True)
        except Service.DoesNotExist:
            check_warning(f"Service not found: {slug}")
            checks.append(False)
    
    return sum(checks) / max(len(checks), 1) * 100


def verify_configuration():
    """Run Django system checks"""
    print_header("DJANGO SYSTEM CHECKS")
    
    try:
        from django.core.management import call_command
        call_command('check')
        check_passed("All Django system checks passed!")
        return 100
    except Exception as e:
        check_failed(f"Django system checks failed: {str(e)}")
        return 0


def main():
    print(f"\n{Colors.BLUE}{'='*60}")
    print("PRODUCTION DEPLOYMENT VERIFICATION".center(60))
    print(f"{'='*60}{Colors.END}\n")
    
    results = {}
    
    # Run all checks
    results['Environment'] = verify_environment()
    results['Security'] = verify_security()
    results['Database'] = verify_database()
    results['Static Files'] = verify_static_files()
    results['Data & Content'] = verify_data()
    results['Django Config'] = verify_configuration()
    
    # Summary
    print_header("DEPLOYMENT READINESS SUMMARY")
    
    total_score = sum(results.values()) / len(results) if results else 0
    
    for category, score in results.items():
        if score >= 80:
            status = f"{Colors.GREEN}✓ {int(score)}%{Colors.END}"
        elif score >= 50:
            status = f"{Colors.YELLOW}⚠ {int(score)}%{Colors.END}"
        else:
            status = f"{Colors.RED}✗ {int(score)}%{Colors.END}"
        
        print(f"{category:.<40} {status}")
    
    print(f"\n{'OVERALL SCORE':.<40} {Colors.BLUE}{int(total_score)}%{Colors.END}")
    
    # Final verdict
    print(f"\n{'='*60}")
    if total_score >= 80:
        check_passed("✓ PROJECT IS READY FOR PRODUCTION DEPLOYMENT")
        sys.exit(0)
    elif total_score >= 60:
        check_warning("⚠ PROJECT NEEDS ATTENTION BEFORE DEPLOYMENT")
        sys.exit(1)
    else:
        check_failed("✗ PROJECT REQUIRES FIXES BEFORE DEPLOYMENT")
        sys.exit(2)


if __name__ == '__main__':
    main()
