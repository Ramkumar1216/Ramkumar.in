@echo off
REM Production Deployment Script for Windows
REM This script prepares your Django project for production deployment

echo.
echo 🚀 Django Portfolio - Production Deployment Script
echo ==================================================
echo.

REM Check if .env file exists
if not exist .env (
    echo ❌ .env file not found!
    echo 📋 Please create .env file from .env.example:
    echo    copy .env.example .env
    echo    Then edit .env with your production settings
    exit /b 1
)

echo 📦 Step 1: Installing dependencies...
pip install -r requirements-prod.txt
if %errorlevel% neq 0 (
    echo ❌ Failed to install dependencies
    exit /b 1
)
echo ✓ Dependencies installed
echo.

echo 🗄️  Step 2: Running database migrations...
python manage.py migrate --noinput
if %errorlevel% neq 0 (
    echo ❌ Failed to run migrations
    exit /b 1
)
echo ✓ Migrations completed
echo.

echo 📊 Step 3: Seeding initial data...
python manage.py create_default_services
if %errorlevel% neq 0 (
    echo ❌ Failed to seed data
    exit /b 1
)
echo ✓ Data seeded
echo.

echo 📁 Step 4: Collecting static files...
python manage.py collectstatic --noinput
if %errorlevel% neq 0 (
    echo ❌ Failed to collect static files
    exit /b 1
)
echo ✓ Static files collected
echo.

echo 🔍 Step 5: Running security checks...
python manage.py check --deploy
echo ✓ Security checks complete
echo.

echo ✅ DEPLOYMENT VERIFICATION
echo =========================
python verify_production.py
echo.

echo 🎉 SUCCESS! Your project is ready to deploy!
echo.
echo 📋 Next steps:
echo    1. Choose your deployment method ^(Docker/Heroku/Server^)
echo    2. Read DEPLOYMENT_GUIDE.md for detailed instructions
echo    3. Deploy using your chosen method
echo    4. Monitor logs after deployment
echo.
echo 📚 For more details, see: DEPLOYMENT_GUIDE.md
echo.
pause
