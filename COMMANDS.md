# Django Portfolio Website - Command Reference

## Quick Commands

### Development Server
```bash
python manage.py runserver
```
Start the development server at http://localhost:8000

### Database Commands
```bash
python manage.py migrate              # Apply migrations
python manage.py makemigrations       # Create migrations
python manage.py migrate --fake-initial  # Reset migrations (use with caution)
python manage.py flush               # Delete all data (resets database)
```

### Admin Commands
```bash
python manage.py createsuperuser     # Create new admin user
python manage.py changepassword <username>  # Change admin password
```

### Static Files
```bash
python manage.py collectstatic       # Collect static files for production
python manage.py collectstatic --clear --noinput  # Force collect
```

### Shell & Scripts
```bash
python manage.py shell               # Interactive Python shell with Django loaded
python create_sample_data.py         # Create sample data (services, testimonials, etc.)
```

### Backup & Restore
```bash
python manage.py dumpdata > backup.json  # Backup all data
python manage.py loaddata backup.json    # Restore from backup
```

## File Descriptions

### Core Project Files
- **manage.py** - Django management commands
- **requirements.txt** - Python dependencies for development
- **requirements-prod.txt** - Production dependencies
- **requirements-dev.txt** - Development tools (black, flake8, pytest)
- **db.sqlite3** - SQLite database (auto-created after migrate)

### Configuration
- **.env.example** - Environment variables template
- **.gitignore** - Git ignore patterns
- **Dockerfile** - Docker container configuration
- **docker-compose.yml** - Docker compose setup

### Documentation
- **README.md** - Complete project documentation
- **QUICK_START.md** - 5-minute quick start guide
- **SETUP_GUIDE.md** - Comprehensive setup instructions
- **CUSTOMIZATION.md** - How to customize the website
- **COMMANDS.md** - This file (command reference)

### Setup Scripts
- **setup.bat** - Automated setup for Windows
- **setup.sh** - Automated setup for Mac/Linux
- **create_sample_data.py** - Script to create sample data

## Project Structure

### Django Apps

#### core/
Home page, about page, testimonials model

Key files:
- `models.py` - Testimonial model
- `views.py` - home(), about() views
- `urls.py` - URL routing

#### services/
Services listing and management

Key files:
- `models.py` - Service model
- `views.py` - services_list() view
- `admin.py` - Service admin configuration
- `urls.py` - Service URLs

#### projects/
Portfolio projects showcase

Key files:
- `models.py` - Project model with detailed fields
- `views.py` - projects_list(), project_detail() views
- `admin.py` - Project admin configuration
- `urls.py` - Project URLs

#### contact/
Contact form and inquiries

Key files:
- `models.py` - Contact model
- `forms.py` - ContactForm for form handling
- `views.py` - contact_view() for form processing
- `admin.py` - Contact admin for viewing messages
- `urls.py` - Contact URLs

#### blog/
Blog posts and articles

Key files:
- `models.py` - Post model
- `views.py` - blog_list(), blog_detail() views
- `admin.py` - Post admin configuration
- `urls.py` - Blog URLs

#### portfolio_project/
Main project configuration

Key files:
- `settings.py` - Django settings and configuration
- `urls.py` - Main URL routing (includes all apps)
- `wsgi.py` - WSGI application for production

### Templates

```
templates/
├── base.html              # Main layout (navbar, footer, CSS)
├── core/
│   ├── home.html         # Homepage with hero, services, projects
│   └── about.html        # About page with timeline
├── services/
│   └── services_list.html # All services with pricing
├── projects/
│   ├── projects_list.html # Project grid
│   └── project_detail.html # Individual project details
├── contact/
│   └── contact.html      # Contact form
└── blog/
    ├── blog_list.html    # Blog post listing
    └── blog_detail.html  # Individual blog post
```

### Static Files

```
static/
├── css/                  # Custom CSS files
├── js/                   # JavaScript files
├── images/               # Images and assets
└── (Tailwind CSS from CDN)
```

### Media Files

```
media/
├── projects/             # Project images
├── blog/                 # Blog post images
└── testimonials/         # Testimonial profile pictures
```

## Database Models

### Service
- title (CharField)
- slug (SlugField, unique)
- description (TextField)
- price (CharField)
- icon (CharField - emoji)
- features (TextField - comma-separated)
- created_at (DateTimeField)

### Project
- title (CharField)
- slug (SlugField, unique)
- description (TextField)
- problem_statement (TextField)
- dataset_used (TextField)
- tools (TextField - comma-separated)
- key_insights (TextField)
- business_result (TextField)
- image (ImageField)
- link (URLField)
- created_at (DateTimeField)
- featured (BooleanField)

### Contact
- name (CharField)
- email (EmailField)
- phone (CharField)
- message (TextField)
- created_at (DateTimeField)
- is_read (BooleanField)

### Testimonial
- name (CharField)
- feedback (TextField)
- rating (IntegerField, 1-5)
- image (ImageField, optional)
- created_at (DateTimeField)

### Post
- title (CharField)
- slug (SlugField, unique)
- author (CharField)
- content (TextField)
- image (ImageField)
- created_at (DateTimeField)
- updated_at (DateTimeField)
- is_published (BooleanField)

## Useful Django Commands

### Python Interactive Shell
```bash
python manage.py shell
```

Examples inside shell:
```python
# Import models
from services.models import Service
from projects.models import Project

# Create a service
Service.objects.create(
    title="Data Analytics",
    slug="data-analytics",
    description="Professional data analysis",
    price="₹999+",
    icon="📊",
    features="Dashboards, Analysis, Reports"
)

# Get all services
services = Service.objects.all()

# Get specific service
service = Service.objects.get(slug="data-analytics")

# Update service
service.price = "₹1299+"
service.save()

# Delete service
service.delete()

# Exit
exit()
```

### Create Superuser (Admin)
```bash
python manage.py createsuperuser
# Follow prompts for username, email, password
```

### Run Tests
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test core
python manage.py test projects

# Run with verbose output
python manage.py test -v 2
```

### Create Backup
```bash
# Export all data to JSON
python manage.py dumpdata > backup.json

# import backup
python manage.py loaddata backup.json
```

## Troubleshooting Commands

### Reset Database (Careful!)
```bash
python manage.py flush  # Deletes all data and asks for confirmation
python manage.py migrate  # Recreate tables
python manage.py createsuperuser  # Create new admin
```

### Fix Migration Issues
```bash
# Show migration status
python manage.py showmigrations

# Rollback specific app migrations
python manage.py migrate <app_name> 0001

# Reset to blank slate (dangerous!)
python manage.py migrate <app_name> zero
```

### Check Settings
```bash
python manage.py diffsettings  # Show settings that differ from defaults
```

### Validate Installation
```bash
python manage.py check  # Check for problems in your installation
```

## Deployment Commands

### Production Build
```bash
# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### Serve with Gunicorn
```bash
gunicorn portfolio_project.wsgi:application --bind 0.0.0.0:8000
```

### Docker Commands
```bash
# Build image
docker build -t portfolio-website .

# Run container
docker run -p 8000:8000 portfolio-website

# Docker Compose
docker-compose up -d  # Start in background
docker-compose down   # Stop containers
docker-compose logs   # View logs
```

## Development Tools

### Code Formatting (Black)
```bash
pip install black
black .  # Format all Python files
```

### Linting (Flake8)
```bash
pip install flake8
flake8 .  # Check code style
```

### Testing (Pytest)
```bash
pip install pytest pytest-django
pytest
```

## Environment Variables

See `.env.example` for all available options.

Common settings:
```
DEBUG=False                    # Production
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgres://...
```

## URL Patterns

### Homepage
- `/` - Home page

### Services
- `/services/` - All services

### Projects
- `/projects/` - All projects
- `/projects/<slug>/` - Project detail

### Contact
- `/contact/` - Contact form

### Blog
- `/blog/` - All blog posts
- `/blog/<slug>/` - Blog post detail

### Admin
- `/admin/` - Django admin panel

---

For more information, see README.md, SETUP_GUIDE.md, or CUSTOMIZATION.md
