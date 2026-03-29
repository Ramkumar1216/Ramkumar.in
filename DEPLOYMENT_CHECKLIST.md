# 🚀 Deployment Checklist - Final Pre-Deploy Review

**Project:** Django Portfolio Website  
**Status:** Production-Ready ✅  
**Last Updated:** Today  

---

## 📋 Pre-Deployment Tasks (Complete Before Running Deploy)

### Configuration & Security ✅
- [ ] Generate new SECRET_KEY (don't use the default in .env.example)
  - Use: https://djecrety.ir/
  - Copy the generated key to .env
- [ ] Create .env file from .env.example
  ```bash
  cp .env.example .env
  nano .env  # Edit with your values
  ```
- [ ] Set DEBUG=False in .env
- [ ] Set ALLOWED_HOSTS to your domain(s)
  ```
  ALLOWED_HOSTS=your-domain.com,www.your-domain.com
  ```
- [ ] Choose database (SQLite for small sites, PostgreSQL for production)
- [ ] If using PostgreSQL:
  - [ ] Install PostgreSQL
  - [ ] Create database and user
  - [ ] Update DATABASE_* variables in .env
- [ ] If using email features:
  - [ ] Set up email provider (Gmail, SendGrid, etc.)
  - [ ] Update EMAIL_* variables in .env
- [ ] Verify no sensitive data in Git
  - [ ] .env file is in .gitignore
  - [ ] No hardcoded secrets in code

### Documentation Review ✅
- [ ] Read PRODUCTION_QUICK_START.md
- [ ] Read DEPLOYMENT_GUIDE.md for your chosen method
- [ ] Understand the 3 deployment options:
  - [ ] Docker (easiest)
  - [ ] Heroku (cloud)
  - [ ] Linux Server (control)

### Choose Deployment Method ✅
- [ ] **Docker**: 5 min setup, no server management
- [ ] **Heroku**: 10 min setup, cloud platform
- [ ] **Linux**: 30-60 min setup, full control
  - [ ] Server provisioned (Ubuntu 20.04+ recommended)
  - [ ] Domain name registered and DNS configured
  - [ ] SSL certificate ready or plan to use Let's Encrypt

### System Requirements Check ✅

#### For All Methods
```bash
# Check Python version (3.9+ required)
python --version
# ✅ Should be 3.9 or higher

# Check Git is installed
git --version
# ✅ Should show version number
```

#### For Docker Method
- [ ] Docker Desktop installed
  ```bash
  docker --version    # Should show Docker version
  docker-compose --version  # Should show version
  ```

#### For Heroku Method
- [ ] Heroku account created (https://www.heroku.com)
- [ ] Heroku CLI installed
  ```bash
  heroku --version   # Should show version
  ```

#### For Linux Server Method
- [ ] Server SSH access working
- [ ] Server has: Python 3.9+, PostgreSQL, Nginx, Supervisor
- [ ] Domain DNS points to server IP
- [ ] Email configured for alerts

---

## 🔧 Pre-Flight Checks (Run These Commands)

### 1. Verify Settings
```bash
# Should show no critical errors
python manage.py check --deploy
```
Expected: Green checkmarks, maybe some yellow warnings

### 2. Run Production Verification Script
```bash
# Should show 95%+ readiness
python verify_production.py
```
Expected: Colored output with high readiness score

### 3. Test with Production Settings
```bash
# Test that settings work with DEBUG=False
DEBUG=False python manage.py runserver
```
Expected: Server starts without errors

### 4. Verify Dependencies
```bash
# Should install without errors
pip install -r requirements-prod.txt
```
Expected: All packages install successfully

---

## 📦 Database Preparation

### SQLite (Small Projects)
```bash
# Just run migrations
python manage.py migrate
python manage.py create_default_services
```

### PostgreSQL (Production Recommended)
```bash
# Via command line (Ubuntu/Linux):
sudo -u postgres psql
CREATE DATABASE portfolio_db;
CREATE USER portfolio_user WITH PASSWORD 'strong_password_here';
ALTER ROLE portfolio_user SET client_encoding TO 'utf8';
ALTER ROLE portfolio_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE portfolio_user SET default_transaction_deferrable TO on;
ALTER ROLE portfolio_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE portfolio_db TO portfolio_user;
\q

# Or use pgAdmin GUI (easier for Windows users)
# Then update .env with:
DATABASE_HOST=localhost
DATABASE_NAME=portfolio_db
DATABASE_USER=portfolio_user
DATABASE_PASSWORD=strong_password_here
DATABASE_PORT=5432
```

After database setup:
```bash
# Run migrations
python manage.py migrate

# Seed initial services
python manage.py create_default_services
```

---

## 📊 Asset Preparation

### Static Files (CSS, JS, Images)
```bash
# Collect all static files
python manage.py collectstatic --noinput
# ✅ Should create staticfiles/ directory

# Verify Whitenoise is working
python manage.py runserver
# Visit http://localhost:8000
# ✅ CSS should load (not look broken)
```

### Media Files (User Uploads)
```bash
# Create media directory if needed
mkdir -p media/
# ✅ Verify it exists
```

---

## 🔐 Security Hardening Verification

```bash
# Run this comprehensive check:
python verify_production.py

# Manually verify:
```

- [ ] SECRET_KEY is unique (not from .env.example)
- [ ] DEBUG=False in production
- [ ] ALLOWED_HOSTS doesn't include wildcards (*)
- [ ] SECURE_SSL_REDIRECT=True in production
- [ ] SESSION_COOKIE_SECURE=True
- [ ] CSRF_COOKIE_SECURE=True
- [ ] Database password is strong and unique
- [ ] No credentials in code, only in .env
- [ ] .env is in .gitignore
- [ ] Admin password is strong (will create during deploy)

---

## 🧪 Testing Before Deployment

### Quick Test
```bash
# Start dev server
python manage.py runserver

# In browser, test:
```
- [ ] Homepage loads: http://localhost:8000
- [ ] Services page: http://localhost:8000/services
- [ ] Individual service: http://localhost:8000/services/data-analytics/
- [ ] Admin panel: http://localhost:8000/admin
- [ ] Contact page: http://localhost:8000/contact
- [ ] Blog page: http://localhost:8000/blog (if available)

### Functionality Test
- [ ] Navigation menu works
- [ ] Links don't have 404 errors
- [ ] Images load correctly
- [ ] CSS styling appears correct
- [ ] Forms are interactive

### Admin Panel Test
- [ ] Can login to admin
- [ ] Can view services
- [ ] Can view projects
- [ ] Can view contacts
- [ ] Can add/edit content (optional test)

---

## 🚀 Deployment Execution Checklist

### For Docker Deployment
```bash
# Go to project root
cd /path/to/portfolio_project

# Run deployment
docker-compose up -d

# Verify
docker-compose ps
docker-compose logs -f web
```
- [ ] Container shows "Up" status
- [ ] No errors in logs
- [ ] Website accessible at your domain

### For Heroku Deployment
```bash
# Login
heroku login

# Create app
heroku create your-app-name

# Set variables
heroku config:set DEBUG=False SECRET_KEY=your-key ALLOWED_HOSTS=your-domain

# Deploy
git push heroku main

# Migrate
heroku run python manage.py migrate
heroku run python manage.py create_default_services

# Check logs
heroku logs --tail
```
- [ ] Build succeeds (no errors in output)
- [ ] App is running
- [ ] Website accessible at https://your-app.herokuapp.com

### For Linux Server Deployment
```bash
# SSH in and follow DEPLOYMENT_GUIDE.md exactly
ssh user@your-domain.com

# Then verify services are running
sudo supervisorctl status
sudo systemctl status nginx
```
- [ ] Gunicorn is running
- [ ] Nginx is running
- [ ] Website accessible at your domain
- [ ] SSL certificate shows as valid

---

## ✅ Post-Deployment Verification

### Immediate Checks (First 5 mins after deploy)
```bash
# Check website loads
curl https://your-domain.com
# ✅ Should return HTML, not error

# Check admin panel
https://your-domain.com/admin
# ✅ Should show login page

# Check services page
https://your-domain.com/services
# ✅ Should display services

# Check static files
# Open DevTools (F12) → Network tab
# ✅ CSS, images should load (200 status)

# Check SSL certificate
# Click lock icon in browser
# ✅ Should say "Secure"

# Check logs for errors
# Docker: docker-compose logs web
# Heroku: heroku logs --tail
# Linux: tail -f logs/django.log
# ✅ Should show minimal errors
```

### Functionality Tests (First 30 mins after deploy)
- [ ] Click all navigation menu items
- [ ] View each service page
- [ ] Submit contact form
- [ ] Verify email received (if email configured)
- [ ] Access admin panel
- [ ] Check responsive design on mobile

### Performance Baseline (First hour)
- [ ] Homepage loads in < 2 seconds
- [ ] Service pages load in < 2 seconds
- [ ] No 500 errors in logs
- [ ] No database connection errors
- [ ] Static files serving efficiently

---

## 📈 Post-Deployment Monitoring (First Week)

### Daily
- [ ] Check application logs for errors
- [ ] Verify website is responsive
- [ ] Test admin panel access
- [ ] Check SSL certificate status

### Weekly
- [ ] Review application logs for patterns
- [ ] Check database size
- [ ] Verify backup procedures (if self-hosted)
- [ ] Check disk space (if self-hosted)

### Monthly
- [ ] Update dependencies
- [ ] Check Django security updates
- [ ] Review access logs
- [ ] Database optimization (if needed)

---

## 🔄 Backup & Disaster Recovery

- [ ] Set up database backups
  - [ ] Docker: Configure backup strategy
  - [ ] Heroku: Enable auto-backup (Postgres)
  - [ ] Linux: Set up daily cron backup job
- [ ] Test backup restore procedure
- [ ] Document recovery steps
- [ ] Keep offsite backup copy

---

## 📊 Success Criteria

Your deployment is **COMPLETE** when:

✅ Website loads without errors  
✅ All pages render correctly  
✅ Admin panel is accessible  
✅ Services display with correct details  
✅ Contact form submits successfully  
✅ CSS/images load (no 404 errors)  
✅ SSL certificate shows as valid  
✅ Application logs show no critical errors  
✅ verify_production.py shows 95%+ readiness  
✅ Response times are acceptable (< 2 sec)  

---

## 🆘 If Something Goes Wrong

1. **Check logs first**
   ```bash
   # Docker
   docker-compose logs -f web
   
   # Heroku
   heroku logs --tail
   
   # Linux
   tail -f logs/django.log
   ```

2. **Run verification script**
   ```bash
   python verify_production.py
   ```

3. **Review troubleshooting section**
   - See DEPLOYMENT_GUIDE.md → Troubleshooting section
   - See PRODUCTION_QUICK_START.md → Common Issues section

4. **Common fixes**
   - Database not accessible: Check DATABASE_* in .env
   - Static files not loading: Run `python manage.py collectstatic --noinput`
   - 502 error: Check if Gunicorn is running
   - 500 error: Check application logs

---

## 📞 Support Resources

- **DEPLOYMENT_GUIDE.md** - Complete step-by-step procedures
- **PRODUCTION_QUICK_START.md** - 5-minute quick start
- **PRODUCTION_READY.md** - Detailed readiness checklist
- **verify_production.py** - Automated verification tool

---

## ✨ Final Notes

- Keep .env file secure and never commit to Git
- Document any custom configurations you make
- Set up monitoring/alerting after deployment
- Plan regular maintenance schedule
- Keep Django and dependencies updated
- Maintain database backups

---

## 🎉 Ready to Deploy?

**Once you've completed this checklist, you're ready to go live!**

Next step:
1. Choose your deployment method (Docker/Heroku/Server)
2. Follow the relevant section in DEPLOYMENT_GUIDE.md
3. Use this checklist to verify each step
4. Monitor logs after deployment

**Your Django portfolio is production-ready. Let's ship it! 🚀**

---

**Deployment Date:** _______________  
**Deployed By:** _______________  
**Notes:** _________________________________________________________________
