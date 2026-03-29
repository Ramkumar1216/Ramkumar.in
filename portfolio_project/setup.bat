@echo off
REM Setup script for Windows

echo.
echo ====== Django Portfolio Website Setup (Windows) ======
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/5] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

echo [2/5] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/5] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo [4/5] Running migrations...
python manage.py migrate
if errorlevel 1 (
    echo ERROR: Failed to run migrations
    pause
    exit /b 1
)

echo [5/5] Creating superuser...
echo.
echo Enter details for admin account:
python manage.py createsuperuser

echo.
echo ====== Setup Complete! ======
echo.
echo To start the development server, run:
echo   venv\Scripts\activate.bat
echo   python manage.py runserver
echo.
echo Then visit: http://localhost:8000
echo Admin panel: http://localhost:8000/admin
echo.
pause
