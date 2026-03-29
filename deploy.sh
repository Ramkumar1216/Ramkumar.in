#!/bin/bash

# Production Deployment Script
# This script prepares your Django project for production deployment

set -e

echo "🚀 Django Portfolio - Production Deployment Script"
echo "=================================================="
echo ""

# Check if .env file exists
if [ ! -f .env ]; then
    echo "❌ .env file not found!"
    echo "📋 Please create .env file from .env.example:"
    echo "   cp .env.example .env"
    echo "   Then edit .env with your production settings"
    exit 1
fi

echo "📦 Step 1: Installing dependencies..."
pip install -r requirements-prod.txt

echo "✓ Dependencies installed"
echo ""

echo "🗄️  Step 2: Running database migrations..."
python manage.py migrate --noinput

echo "✓ Migrations completed"
echo ""

echo "📊 Step 3: Seeding initial data..."
python manage.py create_default_services

echo "✓ Data seeded"
echo ""

echo "📁 Step 4: Collecting static files..."
python manage.py collectstatic --noinput

echo "✓ Static files collected"
echo ""

echo "🔍 Step 5: Running security checks..."
python manage.py check --deploy 2>&1 || echo "⚠️  Some security warnings detected - review above"

echo ""
echo "✓ Security checks complete"
echo ""

echo "✅ DEPLOYMENT VERIFICATION"
echo "========================="
python verify_production.py

echo ""
echo "🎉 SUCCESS! Your project is ready to deploy!"
echo ""
echo "📋 Next steps:"
echo "   1. Choose your deployment method (Docker/Heroku/Server)"
echo "   2. Read DEPLOYMENT_GUIDE.md for detailed instructions"
echo "   3. Deploy using your chosen method"
echo "   4. Monitor logs after deployment"
echo ""
echo "📚 For more details, see: DEPLOYMENT_GUIDE.md"
