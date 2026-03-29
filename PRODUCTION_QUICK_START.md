# Production Deployment Quick Start 🚀

Get your Django portfolio live in 5-30 minutes (depending on deployment method).

---

## ⚡ The Fastest Path (5 Minutes)

### Step 1: Prepare Configuration (2 min)
```bash
# Copy environment template
cp .env.example .env

# Edit .env - CRITICAL CHANGES REQUIRED:
# 1. Generate new SECRET_KEY (search "Django secret key generator")
# 2. Set DEBUG=False
# 3. Set ALLOWED_HOSTS=your-domain.com
# 4. Set DATABASE connection strings (if using PostgreSQL)
```

### Step 2: Run Deployment Script (3 min)
```bash
# Windows:
deploy.bat

# Mac/Linux:
bash deploy.sh
```

**What the script does:**
- ✅ Installs production dependencies
- ✅ Runs database migrations
- ✅ Seeds initial services
- ✅ Collects static files
- ✅ Runs security checks
- ✅ Verifies production readiness

---

## 🎯 Choose Your Deployment Method

### 🐳 Option 1: Docker (Easiest - Recommended)

**Best for:** Quick setup, no server management needed

```bash
# Prerequisites: Install Docker Desktop
# → https://www.docker.com/products/docker-desktop

# One command to start:
docker-compose up -d

# Check status:
docker-compose ps

# View logs:
docker-compose logs -f web
```

**⏱️ Setup time:** ~5 minutes  
**💰 Cost:** Free (or $5-10/month if using managed Docker)  
**📖 Full guide:** See DEPLOYMENT_GUIDE.md → Docker section

---

### ☁️ Option 2: Heroku (Cloud Platform)

**Best for:** Zero infrastructure management, automatic SSL

```bash
# Prerequisites: Create account at heroku.com, install Heroku CLI

heroku login
heroku create your-app-name
heroku config:set DEBUG=False SECRET_KEY=your-key ALLOWED_HOSTS=your-domain.com
git push heroku main
```

**⏱️ Setup time:** ~10 minutes  
**💰 Cost:** Free tier available (or $5-50/month for production)  
**📖 Full guide:** See DEPLOYMENT_GUIDE.md → Heroku section

---

### 🖥️ Option 3: Linux Server (Most Control)

**Best for:** Full control, best performance, custom configuration

```bash
# SSH into your server:
ssh your-domain.com

# Follow detailed step-by-step guide for:
# • Python + PostgreSQL setup
# • Gunicorn + Supervisor configuration
# • Nginx + SSL setup
# • Continuous deployment

# Then start services:
sudo supervisorctl start all
sudo systemctl start nginx
```

**⏱️ Setup time:** ~30-60 minutes  
**💰 Cost:** $5-20/month for VPS  
**📖 Full guide:** See DEPLOYMENT_GUIDE.md → Linux/Ubuntu Server section

---

## 📋 Pre-Deployment Checklist

Before you deploy, ensure these are done:

```bash
# 1. Security check
python verify_production.py
# ✅ Should show 95%+ readiness score

# 2. Django system checks
python manage.py check --deploy
# ✅ Should show only minor warnings

# 3. .env file validation
# ✅ SECRET_KEY is unique and strong
# ✅ DEBUG=False
# ✅ ALLOWED_HOSTS set to your domain
# ✅ DATABASE credentials correct
```

### Minimum .env Configuration

```env
# Django
DEBUG=False
SECRET_KEY=your-unique-secret-key-here
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
ENVIRONMENT=production

# Database (PostgreSQL recommended for production)
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=portfolio_db
DATABASE_USER=postgres
DATABASE_PASSWORD=your-very-secure-password
DATABASE_HOST=your-database-host
DATABASE_PORT=5432
```

⚠️ **CRITICAL**: Generate a new SECRET_KEY! Don't use the one in .env.example!

---

## 🚀 Deployment by Method

### Docker Deployment

```bash
# Step 1: Ensure Docker is running
# Open Docker Desktop

# Step 2: In project root, run:
docker-compose up -d

# Step 3: Verify it's running
docker-compose ps
# You should see "web" container as "Up"

# Step 4: Check logs for errors
docker-compose logs -f web

# Step 5: Visit http://your-domain (or localhost:8000)
```

**That's it!** Docker handles everything.

---

### Heroku Deployment

```bash
# Step 1: Install Heroku CLI
# → https://devcenter.heroku.com/articles/heroku-cli

# Step 2: Login
heroku login

# Step 3: Create app
heroku create your-portfolio-app

# Step 4: Set environment variables (one per line)
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-secret-key
heroku config:set ALLOWED_HOSTS=your-app.herokuapp.com

# Step 5: Deploy
git push heroku main

# Step 6: Run migrations
heroku run python manage.py migrate

# Step 7: Seed data
heroku run python manage.py create_default_services

# Step 8: Visit https://your-app.herokuapp.com
```

**Note:** Heroku auto-provides SSL/HTTPS. Your app is immediately secure!

---

### Linux Server Deployment

See **DEPLOYMENT_GUIDE.md → Linux/Ubuntu Server section** for complete step-by-step guide.

Quick summary:
1. Provision Ubuntu server (20.04 or 22.04 LTS recommended)
2. Install Python, PostgreSQL, Nginx, Supervisor
3. Clone repository and set up virtual environment
4. Configure environment variables in .env
5. Run migrations and seed data
6. Configure Gunicorn with Supervisor
7. Configure Nginx as reverse proxy
8. Set up SSL with Let's Encrypt
9. Start services and verify

---

## ✅ Post-Deployment Verification

After deploying, test these to ensure everything works:

```bash
# 1. Website loads
curl https://your-domain.com
# ✅ Should return HTML (not 500 error)

# 2. Admin panel accessible
https://your-domain.com/admin
# ✅ Should show login page

# 3. Services page works
https://your-domain.com/services
# ✅ Should display all services

# 4. Individual service pages
https://your-domain.com/services/data-analytics/
# ✅ Should show service details

# 5. Static files loading
# Open DevTools (F12) → Network tab
# ✅ CSS, images should load (no 404 errors)

# 6. SSL certificate valid
# Click lock icon in address bar
# ✅ Should say "Secure" or "This site is secure"
```

---

## 🔍 Monitoring & Logs

### Docker
```bash
# View logs
docker-compose logs -f web

# Stop application
docker-compose down

# Restart application
docker-compose up -d
```

### Heroku
```bash
# View logs
heroku logs --tail

# Run Django management command
heroku run python manage.py migrate

# SSH into app
heroku ps:exec

# View app status
heroku apps:info
```

### Linux Server
```bash
# View Django logs
tail -f logs/django.log

# Check Gunicorn status
sudo supervisorctl status

# Check Nginx status
sudo systemctl status nginx

# View Nginx logs
tail -f /var/log/nginx/error.log
```

---

## 🆘 Common Issues & Solutions

### "502 Bad Gateway" Error
**Linux only** - Application server not running
```bash
sudo supervisorctl restart gunicorn
sudo systemctl status nginx
```

### "Database Connection Refused"
```bash
# Check DATABASE_* variables in .env
nano .env

# Ensure PostgreSQL is running
sudo systemctl status postgresql

# Verify database exists
sudo -u postgres psql -l
```

### "Static Files Not Loading"
```bash
# Collect static files
python manage.py collectstatic --noinput

# Docker:
docker-compose exec web python manage.py collectstatic --noinput

# Heroku:
heroku run python manage.py collectstatic --noinput
```

### "SECRET_KEY or DEBUG Exposed"
Run automated check:
```bash
python verify_production.py
# Should show minimal warnings
```

**Full troubleshooting guide:** See DEPLOYMENT_GUIDE.md → Troubleshooting section

---

## 📈 Next Steps After Deployment

### First Week
- ✅ Monitor application logs for errors
- ✅ Test all functionality (services, contact form, admin)
- ✅ Verify SSL certificate auto-renewal (if using Let's Encrypt)
- ✅ Check email notifications are working

### Monthly Maintenance
- ✅ Update dependencies: `pip install -r requirements-prod.txt --upgrade`
- ✅ Check Django security updates
- ✅ Review application logs for issues
- ✅ Backup database (if self-hosted)

### Code Updates
After each code change:
```bash
# Docker
git pull
docker-compose up -d

# Heroku
git push heroku main

# Linux
git pull
sudo supervisorctl restart gunicorn
```

---

## 📚 Complete Documentation

- **DEPLOYMENT_GUIDE.md** - In-depth procedures for all 3 deployment methods
- **PRODUCTION_READY.md** - 100-item production readiness checklist
- **verify_production.py** - Automated security and configuration verification

---

## 🎯 Success Indicators

Your deployment is successful when:

- ✅ Website loads without errors
- ✅ All pages render correctly
- ✅ Admin panel is accessible
- ✅ Service pages show correct details
- ✅ Contact form can submit
- ✅ SSL certificate shows as valid
- ✅ Logs show no critical errors
- ✅ `verify_production.py` shows high readiness score

---

## 🚀 Ready to Deploy?

**Choose your method above and follow the steps for your platform.**

**Questions?**
1. Read DEPLOYMENT_GUIDE.md for your deployment method
2. Run `python verify_production.py` for diagnostics
3. Check sections in this file marked 🆘 for common issues

**You've got this!** Your Django portfolio is ready for production. 🎉
