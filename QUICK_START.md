# Quick Start Guide ⚡

Get your Django portfolio website running in 5 minutes!

## For Windows Users

### Option 1: Automated Setup (Easiest)

1. **Open Command Prompt** in the project folder
2. **Double-click** `setup.bat`
3. Follow the prompts to create admin account
4. The server starts automatically!

### Option 2: Manual Setup

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create admin account
python manage.py createsuperuser

# 6. Run server
python manage.py runserver
```

## For Mac/Linux Users

### Option 1: Automated Setup (Easiest)

1. **Open Terminal** in the project folder
2. **Run**: `chmod +x setup.sh && ./setup.sh`
3. Follow the prompts
4. Done!

### Option 2: Manual Setup

```bash
# 1. Create virtual environment
python3 -m venv venv

# 2. Activate virtual environment
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create admin account
python manage.py createsuperuser

# 6. Run server
python manage.py runserver
```

## Access Your Website

🌐 **Website**: http://localhost:8000
🔐 **Admin Panel**: http://localhost:8000/admin

Use the credentials from Step 5 (superuser) to login to admin panel.

## Add Your First Content

### 1. Add a Service

1. Go to http://localhost:8000/admin
2. Click "Services" → "Add Service"
3. Fill the form:
   - Title: "Data Analytics"
   - Slug: "data-analytics"
   - Description: "I provide comprehensive data analysis services..."
   - Price: "₹999+"
   - Icon: "📊"
   - Features: "Custom reports, Data cleaning, Visualization, Consultation"
4. Click "Save"

### 2. Add a Project

1. Go to Admin Panel
2. Click "Projects" → "Add Project"
3. Fill the form:
   - Title: "Sales Dashboard Project"
   - Slug: "sales-dashboard"
   - Description: "Built a comprehensive sales analytics dashboard..."
   - Tools: "Python, Power BI, SQL"
   - Upload an image (jpg/png)
4. Click "Save"

### 3. Add a Testimonial

1. Go to Admin Panel
2. Click "Testimonials" → "Add Testimonial"
3. Fill:
   - Name: "Client Name"
   - Feedback: "Ramkumar is amazing! He helped us..."
   - Rating: 5
4. Click "Save"

## Next Steps

1. **Customize Your Info**
   - Open `templates/base.html`
   - Change WhatsApp numbers
   - Change email address
   - Update social media links

2. **Add More Projects**
   - Go to Admin → Projects → Add Project
   - Add 3-5 projects to showcase

3. **Add Services**
   - Go to Admin → Services → Add Service
   - Add your main services

4. **Write Blog Posts**
   - Go to Admin → Posts → Add Post
   - Write about your expertise

## Troubleshooting

### Problem: "Port 8000 in use"
```bash
python manage.py runserver 8001
```

### Problem: "No module named 'django'"
- Make sure virtual environment is activated
- Run: `pip install -r requirements.txt`

### Problem: "Database error"
```bash
python manage.py migrate
```

## Deployment

When ready to go live:

1. Change `DEBUG = False` in `settings.py`
2. Update `ALLOWED_HOSTS` with your domain
3. Deploy to Heroku, AWS, or other platform

For detailed deployment instructions, see README.md

---

**You're all set! 🎉 Start adding content to your portfolio!**
