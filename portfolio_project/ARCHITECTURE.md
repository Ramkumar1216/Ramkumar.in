# Project Architecture & File Structure

## 📊 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    CLIENT (Browser)                          │
│                                                              │
│  http://localhost:8000                                      │
└───────────────────────┬─────────────────────────────────────┘
                        │ HTTP Request/Response
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                    DJANGO SERVER (Backend)                   │
│                                                              │
│  ┌────────────────────────────────────────────────────┐   │
│  │  settings.py - Django Configuration               │   │
│  │  - DEBUG = True/False                              │   │
│  │  - INSTALLED_APPS (5 apps)                         │   │
│  │  - DATABASE configuration                          │   │
│  │  - STATIC/MEDIA settings                           │   │
│  └────────────────────────────────────────────────────┘   │
│                        ▼                                    │
│  ┌────────────────────────────────────────────────────┐   │
│  │  urls.py - URL Routing                             │   │
│  │  - / → core (home)                                 │   │
│  │  - /about → core (about)                           │   │
│  │  - /services/ → services (list)                    │   │
│  │  - /projects/ → projects (list & detail)          │   │
│  │  - /contact/ → contact (form)                      │   │
│  │  - /blog/ → blog (list & detail)                   │   │
│  │  - /admin/ → Django admin                          │   │
│  └────────────────────────────────────────────────────┘   │
│                        ▼                                    │
│  ┌────────────────────────────────────────────────────┐   │
│  │  5 Django Apps                                     │   │
│  │  ├─ core (home, about, testimonials)              │   │
│  │  ├─ services (service listings)                   │   │
│  │  ├─ projects (portfolio projects)                 │   │
│  │  ├─ contact (inquiry form)                        │   │
│  │  └─ blog (blog posts)                             │   │
│  │                                                    │   │
│  │  Each app contains:                               │   │
│  │  - models.py (Database schemas)                   │   │
│  │  - views.py (Business logic)                      │   │
│  │  - urls.py (URL pattern)                          │   │
│  │  - admin.py (Admin interface)                     │   │
│  │  - forms.py (if needed)                           │   │
│  └────────────────────────────────────────────────────┘   │
│                        ▼                                    │
│  ┌────────────────────────────────────────────────────┐   │
│  │  Templates (HTML - Jinja2)                         │   │
│  │  - base.html (navbar, footer, CSS)                │   │
│  │  - 8 page templates                               │   │
│  │  - Template tags and filters                       │   │
│  │  - Static file includes                           │   │
│  └────────────────────────────────────────────────────┘   │
│                        ▼                                    │
│  ┌────────────────────────────────────────────────────┐   │
│  │  Database Layer                                    │   │
│  │  - SQLite3 (dev) / PostgreSQL (prod)              │   │
│  │  - 5 Models with fields                           │   │
│  │  - Migrations applied                             │   │
│  │  - ORM queries via Django                         │   │
│  └────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                    DATABASE                                  │
│                                                              │
│  Service (Service model)                                    │
│  ├─ id, title, slug, description                          │
│  ├─ price, icon, features, created_at                     │
│                                                              │
│  Project (Project model)                                    │
│  ├─ id, title, slug, description                          │
│  ├─ problem_statement, dataset_used, tools                │
│  ├─ key_insights, business_result, image                  │
│  ├─ link, featured, created_at                            │
│                                                              │
│  Contact (Contact model)                                    │
│  ├─ id, name, email, phone, message                       │
│  ├─ is_read, created_at                                   │
│                                                              │
│  Testimonial (Testimonial model)                           │
│  ├─ id, name, feedback, rating, image                     │
│  ├─ created_at                                            │
│                                                              │
│  Post (Blog Post model)                                    │
│  ├─ id, title, slug, author, content                      │
│  ├─ image, is_published, created_at, updated_at           │
└─────────────────────────────────────────────────────────────┘
```

## 📁 Complete File Structure

```
portfolio_project/
│
├── 📖 Documentation (8 files)
│   ├── START_HERE.md ⭐ (Main entry point)
│   ├── QUICK_START.md (5-minute setup)
│   ├── SETUP_GUIDE.md (Detailed guide)
│   ├── CUSTOMIZATION.md (Personalization)
│   ├── README.md (Full documentation)
│   ├── COMMANDS.md (Django commands)
│   ├── INDEX.md (Project overview)
│   ├── DELIVERY_SUMMARY.md (Features list)
│   └── VERIFICATION_CHECKLIST.md (QA checklist)
│
├── ⚙️ Configuration (5 files)
│   ├── manage.py (Django CLI)
│   ├── requirements.txt (Dependencies)
│   ├── requirements-prod.txt (Production deps)
│   ├── requirements-dev.txt (Dev tools)
│   └── .env.example (Environment template)
│
├── 🗂️ portfolio_project/ (Main project)
│   ├── __init__.py
│   ├── settings.py (Django config)
│   ├── urls.py (Main routing)
│   └── wsgi.py (Production server)
│
├── 🧩 core/ (Home & About app)
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py (Testimonial)
│   ├── views.py (home, about)
│   ├── urls.py
│   ├── admin.py (Admin config)
│   ├── tests.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│
├── 🛒 services/ (Services app)
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py (Service)
│   ├── views.py (services_list)
│   ├── urls.py
│   ├── admin.py (Admin config)
│   ├── tests.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│
├── 📁 projects/ (Portfolio app)
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py (Project)
│   ├── views.py (list, detail)
│   ├── urls.py
│   ├── admin.py (Admin config)
│   ├── tests.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│
├── 📧 contact/ (Contact app)
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py (Contact)
│   ├── forms.py (ContactForm)
│   ├── views.py (contact view)
│   ├── urls.py
│   ├── admin.py (Admin config)
│   ├── tests.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│
├── 📝 blog/ (Blog app)
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py (Post)
│   ├── views.py (list, detail)
│   ├── urls.py
│   ├── admin.py (Admin config)
│   ├── tests.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│
├── 🎨 templates/ (HTML 9 files)
│   ├── base.html (Main layout)
│   ├── core/
│   │   ├── home.html (Homepage)
│   │   └── about.html (About page)
│   ├── services/
│   │   └── services_list.html (All services)
│   ├── projects/
│   │   ├── projects_list.html (Projects grid)
│   │   └── project_detail.html (Project page)
│   ├── contact/
│   │   └── contact.html (Contact form)
│   ├── blog/
│   │   ├── blog_list.html (Blog listing)
│   │   └── blog_detail.html (Individual post)
│
├── 📦 static/ (CSS, JS, images)
│   ├── css/ (Custom CSS)
│   ├── js/ (JavaScript)
│   └── images/ (Icons, assets)
│
├── 💾 media/ (User uploads)
│   ├── projects/ (Project images)
│   ├── blog/ (Blog images)
│   └── testimonials/ (Testimonial photos)
│
├── 🔧 Docker & Deployment
│   ├── Dockerfile (Container config)
│   └── docker-compose.yml (Full stack)
│
├── 🚀 Setup Scripts
│   ├── setup.bat (Windows setup)
│   ├── setup.sh (Mac/Linux setup)
│   └── create_sample_data.py (Sample data)
│
├── 🔐 Security & Git
│   ├── .env (Environment - create after setup)
│   ├── .gitignore (Git patterns)
│   └── db.sqlite3 (Database - auto-created)
│
└── 📋 Additional
    └── (All documentation files)
```

## 🔄 Request Flow Diagram

```
User visits website
        │
        ▼
URL gets matched to pattern (urls.py)
        │
        ├─ / → core.views.home()
        ├─ /about/ → core.views.about()
        ├─ /services/ → services.views.services_list()
        ├─ /projects/ → projects.views.projects_list()
        ├─ /projects/<slug>/ → projects.views.project_detail()
        ├─ /contact/ → contact.views.contact_view()
        ├─ /blog/ → blog.views.blog_list()
        ├─ /blog/<slug>/ → blog.views.blog_detail()
        └─ /admin/ → Django admin
        │
        ▼
View function called
        │
        ├─ Fetch data from database via models
        ├─ Process form data (if form submitted)
        ├─ Prepare context dictionary
        │
        ▼
Template rendered
        │
        ├─ Load base.html (navbar, footer, CSS)
        ├─ Include specific page template
        ├─ Replace {{ variables }} with context data
        ├─ Include static files (CSS, JS)
        │
        ▼
HTML sent to browser
        │
        ▼
Browser renders page
        │
        ▼
User sees your portfolio! 🎉
```

## 🗄️ Database Relationships

```
Service Model
├─ id (Primary Key)
├─ title (CharField)
├─ slug (SlugField - Unique)
├─ description (TextField)
├─ price (CharField)
├─ icon (CharField)
├─ features (TextField)
└─ created_at (DateTimeField)

Project Model
├─ id (Primary Key)
├─ title (CharField)
├─ slug (SlugField - Unique)
├─ description (TextField)
├─ problem_statement (TextField)
├─ dataset_used (TextField)
├─ tools (TextField)
├─ key_insights (TextField)
├─ business_result (TextField)
├─ image (ImageField)
├─ link (URLField)
├─ featured (BooleanField)
└─ created_at (DateTimeField)

Contact Model
├─ id (Primary Key)
├─ name (CharField)
├─ email (EmailField)
├─ phone (CharField)
├─ message (TextField)
├─ is_read (BooleanField)
└─ created_at (DateTimeField)

Testimonial Model
├─ id (Primary Key)
├─ name (CharField)
├─ feedback (TextField)
├─ rating (IntegerField 1-5)
├─ image (ImageField)
└─ created_at (DateTimeField)

Post (Blog) Model
├─ id (Primary Key)
├─ title (CharField)
├─ slug (SlugField - Unique)
├─ author (CharField)
├─ content (TextField)
├─ image (ImageField)
├─ is_published (BooleanField)
├─ created_at (DateTimeField)
└─ updated_at (DateTimeField)
```

## 🛠️ Technology Stack Diagram

```
Frontend Layer
├─ HTML5 Templates
├─ CSS3 (Tailwind CSS 3)
├─ JavaScript (minimal for animations)
└─ Responsive Design (Mobile First)

Backend Layer
├─ Django 4.2.7 (Web Framework)
├─ Python 3.8+ (Language)
├─ Pillow (Image Processing)
└─ Django Forms (Form Handling)

Database Layer
├─ SQLite3 (Development)
├─ PostgreSQL (Production Optional)
└─ Django ORM (Object-Relational Mapping)

Deployment Layer
├─ Gunicorn (WSGI Server)
├─ Docker (Containerization)
├─ Environment Variables (.env)
└─ Static File Collection

Admin/Management Layer
├─ Django Admin Panel
├─ Custom ModelAdmin Classes
├─ Search & Filter
└─ List Displays
```

## 📊 File Count Summary

```
Documentation Files: 9
Configuration Files: 8
Django Project Files: 4
App Files (core): 8
App Files (services): 8
App Files (projects): 8
App Files (contact): 9
App Files (blog): 8
Template Files: 9
Deployment Files: 2
Setup Scripts: 2
Utility Scripts: 1
─────────────────────
Total: 86 Files Created!
```

## 🎯 Key Paths

```
Home: /
About: /about/
Services: /services/
Projects: /projects/
Project Detail: /projects/<slug>/
Contact: /contact/
Blog: /blog/
Blog Detail: /blog/<slug>/
Admin: /admin/
```

---

**This comprehensive architecture supports everything you need for a professional portfolio website!**
