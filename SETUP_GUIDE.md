# Portfolio Website - Complete Setup Guide

## 📦 What You're Getting

A **production-ready Django portfolio website** with:
- ✅ Modern dark-themed UI with animations
- ✅ Fully responsive design (mobile, tablet, desktop)
- ✅ Database-driven content management
- ✅ Django Admin Panel for easy updates
- ✅ Services, Projects, Blog, and Contact sections
- ✅ WhatsApp integration
- ✅ Image upload capabilities
- ✅ Professional code structure

## 🚀 Installation (Choose One Method)

### Method 1: Automated Setup (⭐ Recommended)

**Windows Users:**
```
Double-click: setup.bat
```

**Mac/Linux Users:**
```bash
chmod +x setup.sh
./setup.sh
```

This will automatically:
1. Create virtual environment
2. Install dependencies
3. Set up database
4. Create admin account

### Method 2: Manual Setup (10-15 minutes)

**Step 1: Create Virtual Environment**

Windows:
```cmd
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

**Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 3: Setup Database**
```bash
python manage.py migrate
```

**Step 4: Create Admin Account**
```bash
python manage.py createsuperuser
```

Follow the prompts to set:
- Username
- Email
- Password (choose strong password)

**Step 5: Start Development Server**
```bash
python manage.py runserver
```

## 🌐 Access Your Website

Once running:

- **Website**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin
- **Login**: Use credentials from admin account

## 📝 First Steps: Adding Content

### 1. Add Your Basic Info

**File**: `templates/base.html`

Find and replace:
```
9876543210  → Your WhatsApp number
ramkumar@example.com → Your email
Ramkumar → Your name
```

### 2. Add a Service

1. Go to Admin Panel (http://localhost:8000/admin)
2. Click **Services** → **Add Service**
3. Fill form:
   - **Title**: "Data Analytics"
   - **Slug**: "data-analytics" (auto from title)
   - **Description**: "I help businesses understand their data..."
   - **Price**: "₹999+"
   - **Icon**: "📊" (or any emoji)
   - **Features**: "Custom dashboards, Analysis, Reports" (comma-separated)
4. Click **Save**

### 3. Add a Project

1. Go to Admin Panel → **Projects** → **Add Project**
2. Fill form:
   - **Title**: "Sales Analytics Dashboard"
   - **Slug**: "sales-dashboard"
   - **Description**: "Built a comprehensive sales tracking system..."
   - **Tools**: "Python, Power BI, SQL" (comma-separated)
   - **Problem Statement**: "Client needed real-time sales visibility..."
   - **Business Result**: "Increased sales tracking accuracy by 95%"
   - **Image**: Upload a screenshot (1200x600px ideal)
3. Click **Save**

### 4. Add a Testimonial

1. Go to Admin Panel → **Testimonials** → **Add Testimonial**
2. Fill:
   - **Name**: "Client Name"
   - **Feedback**: "Great work! Amazing results!"
   - **Rating**: 5 ⭐
3. Click **Save**

### 5. Write Blog Post

1. Go to Admin Panel → **Posts** → **Add Post**
2. Fill:
   - **Title**: "How to Use Data for Marketing"
   - **Slug**: "data-marketing" (auto)
   - **Content**: Write your article
   - **Author**: Your name (default: Ramkumar)
   - **Is Published**: ✓ Check this box
3. Click **Save**

## 💻 Project Structure

```
portfolio_project/
├── manage.py                 # Django management commands
├── requirements.txt          # Python dependencies
├── README.md                 # Full documentation
├── QUICK_START.md            # Quick setup guide
├── CUSTOMIZATION.md          # How to customize
│
├── portfolio_project/        # Main Django project
│   ├── settings.py          # Configuration
│   ├── urls.py              # Main routing
│   └── wsgi.py              # Production server
│
├── core/                     # Home & About
├── services/                 # Services listing
├── projects/                 # Portfolio projects
├── contact/                  # Contact form
├── blog/                     # Blog posts
│
├── templates/                # HTML files
│   ├── base.html            # Main layout
│   ├── core/
│   ├── services/
│   ├── projects/
│   ├── contact/
│   └── blog/
│
├── static/                   # CSS, JS, images
│   ├── css/
│   ├── js/
│   └── images/
│
└── media/                    # User uploads
    ├── projects/
    ├── blog/
    └── testimonials/
```

## 🎨 Customization Quick Links

| What to Change | Where to Find |
|---|---|
| Website colors | `templates/base.html` CSS section |
| Your name/title | `templates/base.html` and `templates/core/home.html` |
| WhatsApp number | Search for `wa.me/919876543210` in all files |
| Email address | `templates/contact/contact.html` |
| About section | Admin Panel or `templates/core/about.html` |
| Social media links | `templates/base.html` footer |

**See CUSTOMIZATION.md for detailed instructions!**

## 🔐 Admin Panel Guide

### Managing Services
- Services appear on home page and services page
- Drag to reorder (in admin)
- Edit anytime to update pricing

### Managing Projects
- Mark "featured" to show on home page
- Upload project images (1200x600px recommended)
- Include tools, problems, and results

### Managing Blog Posts
- Create rich content with line breaks
- Set `is_published` to control visibility
- Automatically shows latest posts first

### Contact Messages
- View all form submissions in Admin
- Mark as "read" to track inquiries
- Export or reply to messages

## 🚀 Deployment Checklist

Ready to make it live?

- [ ] Change `DEBUG = False` in `settings.py`
- [ ] Set `SECRET_KEY` to secure random value
- [ ] Update `ALLOWED_HOSTS` with your domain
- [ ] Set up database (PostgreSQL recommended)
- [ ] Configure static files for production
- [ ] Set up SSL/HTTPS
- [ ] Add your 10+ projects
- [ ] Write 5+ blog posts
- [ ] Add customer testimonials
- [ ] Test all forms and links

Deploy to:
- **Heroku** (easiest)
- **AWS** (scalable)
- **PythonAnywhere** (beginner-friendly)
- **DigitalOcean** (affordable)

## ❓ Common Questions

**Q: How do I change colors?**
A: Edit `.gradient-bg` CSS in `templates/base.html`

**Q: Can I add more services?**
A: Yes! Admin Panel → Services → Add Service

**Q: How do I upload project images?**
A: Admin Panel → Projects → Add Project → Upload image field

**Q: Can I use my own domain?**
A: Yes! Deploy to hosting and point domain to server.

**Q: How do I backup my data?**
A: Download `db.sqlite3` file (or export from database)

## 📞 Support and Resources

- **Django Docs**: https://docs.djangoproject.com/
- **Tailwind CSS**: https://tailwindcss.com/docs
- **Python**: https://www.python.org/
- **Deploy Guide**: README.md
- **Customization**: CUSTOMIZATION.md

## 🎯 Next Steps

1. **Weekend**: Setup + add 5 projects
2. **Week 1**: Write 3 blog posts + get testimonials
3. **Week 2**: Customize colors + deploy
4. **Ongoing**: Update content regularly

---

## 🎉 You're Ready!

Your professional portfolio website is ready to impress clients and land new projects.

**Questions?** Check README.md or CUSTOMIZATION.md

**Let's go! 🚀**
