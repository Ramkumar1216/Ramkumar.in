# 🚀 PRODUCTION DEPLOYMENT GUIDE

**Status**: Production Ready ✅

This guide covers everything needed to deploy your Django portfolio website to production.

---

## 📋 PRE-DEPLOYMENT CHECKLIST

### Security
- [ ] Generate a new `SECRET_KEY` (use `django-insecure-secret-key-generator`)
- [ ] Create `.env` file from `.env.example`
- [ ] Set `DEBUG=False` in production
- [ ] Update `ALLOWED_HOSTS` with your domain(s)
- [ ] Set `ENVIRONMENT=production`
- [ ] Disable `ALLOWED_HOSTS=['*']` (use specific domains only)
- [ ] Review CSRF settings for your domain
- [ ] Configure SSL/TLS certificate

### Database
- [ ] Choose database backend (PostgreSQL recommended for production)
- [ ] Configure database credentials in `.env`
- [ ] Run migrations: `python manage.py migrate`
- [ ] Seed initial data: `python manage.py create_default_services`
- [ ] Set up database backups

### Static Files
- [ ] Run `python manage.py collectstatic` (whitenoise will handle compression)
- [ ] Configure static file serving (whitenoise for Gunicorn)
- [ ] Test static file loading

### Media Files
- [ ] Ensure `/media` directory is writable
- [ ] Configure media file permissions
- [ ] Set up media file backups

### Email Configuration
- [ ] Configure SMTP settings in `.env`
- [ ] Test email sending
- [ ] Add SPF/DKIM records for your domain

### Logging
- [ ] Create `/logs` directory with proper permissions
- [ ] Configure log rotation
- [ ] Monitor logs regularly

### Testing
- [ ] Run `python manage.py check --deploy`
- [ ] Test all URLs and services
- [ ] Test contact form submission
- [ ] Test WhatsApp integration
- [ ] Test admin panel access

---

## 🐳 DEPLOYMENT OPTIONS

### **Option 1: Docker + Docker Compose (Recommended)**

```bash
# Build and run with Docker
docker-compose up -d

# Run migrations inside container
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py create_default_services
docker-compose exec web python manage.py collectstatic --noinput

# View logs
docker-compose logs -f web
```

### **Option 2: Heroku**

```bash
# Install Heroku CLI
# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Set environment variables
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-generated-secret-key
heroku config:set ALLOWED_HOSTS=your-domain.com

# Push code
git push heroku main

# Run migrations
heroku run python manage.py migrate
heroku run python manage.py create_default_services

# View logs
heroku logs --tail
```

### **Option 3: Linux Server (Ubuntu/Debian)**

#### Step 1: Server Setup
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y python3-pip python3-venv postgresql postgresql-contrib nginx supervisor

# Create application directory
sudo mkdir -p /var/www/portfolio
cd /var/www/portfolio

# Clone or transfer your code
git clone your-repo-url .

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements-prod.txt
```

#### Step 2: Database Configuration
```bash
# Create PostgreSQL database
sudo -u postgres psql
CREATE DATABASE portfolio_db;
CREATE USER portfolio_user WITH PASSWORD 'secure-password';
ALTER ROLE portfolio_user SET client_encoding TO 'utf8';
ALTER ROLE portfolio_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE portfolio_db TO portfolio_user;
\q

# Run migrations
python manage.py migrate
python manage.py create_default_services
python manage.py collectstatic --noinput
```

#### Step 3: Gunicorn Setup
```bash
# Create gunicorn startup script
sudo nano /var/www/portfolio/gunicorn_start.sh

# Content:
#!/bin/bash
NAME="portfolio_app"
DJANGODIR=/var/www/portfolio
USER=www-data
GROUP=www-data
WORKERS=3
WORKER_CLASS=sync
WORKER_TIMEOUT=30
BIND=0.0.0.0:8001

cd $DJANGODIR
source venv/bin/activate
exec gunicorn \
  --name $NAME \
  --workers $WORKERS \
  --worker-class $WORKER_CLASS \
  --worker-timeout $WORKER_TIMEOUT \
  --bind $BIND \
  --log-level info \
  portfolio_project.wsgi:application

# Make executable
sudo chmod +x /var/www/portfolio/gunicorn_start.sh
```

#### Step 4: Supervisor Configuration
```bash
# Create supervisor config
sudo nano /etc/supervisor/conf.d/portfolio.conf

# Content:
[program:portfolio]
command=/var/www/portfolio/gunicorn_start.sh
user=www-data
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/portfolio/gunicorn.log

# Create log directory
sudo mkdir -p /var/log/portfolio
sudo chown www-data:www-data /var/log/portfolio

# Start supervisor
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start portfolio
```

#### Step 5: Nginx Configuration
```bash
# Create Nginx config
sudo nano /etc/nginx/sites-available/portfolio

# Content:
upstream portfolio_app {
    server 127.0.0.1:8001;
}

server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    client_max_body_size 25M;

    # Redirect HTTP to HTTPS (after SSL setup)
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;
    
    # SSL certificates (from Let's Encrypt)
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    
    client_max_body_size 25M;

    location / {
        proxy_pass http://portfolio_app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /var/www/portfolio/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location /media/ {
        alias /var/www/portfolio/media/;
        expires 7d;
    }
}

# Enable the site
sudo ln -s /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled/portfolio
sudo nginx -t
sudo systemctl restart nginx
```

#### Step 6: SSL Certificate (Let's Encrypt)
```bash
# Install certbot
sudo apt install -y certbot python3-certbot-nginx

# Get certificate
sudo certbot certonly --standalone -d yourdomain.com -d www.yourdomain.com

# Auto-renewal
sudo systemctl enable certbot.timer
sudo systemctl start certbot.timer
```

---

## 🔍 POST-DEPLOYMENT VERIFICATION

```bash
# Check Django System Checks
python manage.py check --deploy

# Verify Static Files
python manage.py collectstatic --dry-run

# Test Database Connection
python manage.py dbshell

# Verify Services
python manage.py shell
# Inside shell:
from services.models import Service
Service.objects.all()

# Check Gunicorn
ps aux | grep gunicorn

# Check Supervisor
sudo supervisorctl status

# Test Website
curl https://yourdomain.com
```

---

## 📊 PRODUCTION MONITORING

### Essential Metrics to Monitor
- Application response time
- Error rate and types
- Database connection pool usage
- Memory usage
- Disk space
- Static file caching efficiency

### Useful Tools
- **Error Tracking**: Sentry
- **Performance Monitoring**: New Relic
- **Uptime Monitoring**: Better Uptime or StatusCake
- **Log Management**: ELK Stack or Papertrail

---

## 🔄 CONTINUOUS DEPLOYMENT

### GitHub Actions Example
```yaml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Run Tests
        run: python manage.py test
      
      - name: Deploy to Server
        run: |
          ssh user@server.com << 'EOF'
          cd /var/www/portfolio
          git pull origin main
          source venv/bin/activate
          pip install -r requirements-prod.txt
          python manage.py migrate
          python manage.py collectstatic --noinput
          sudo supervisorctl restart portfolio
          EOF
```

---

## 🆘 TROUBLESHOOTING

### 500 Internal Server Error
```bash
# Check logs
sudo supervisorctl tail portfolio
docker-compose logs -f web

# Check permissions
sudo chown -R www-data:www-data /var/www/portfolio

# Verify environment variables
python manage.py shell
from django.conf import settings
print(settings.DEBUG)
```

### Static Files Not Loading
```bash
# Recollect static files
python manage.py collectstatic --clear --noinput

# Check permissions
sudo chown -R www-data:www-data /var/www/portfolio/staticfiles

# Verify Nginx config
sudo nginx -t
```

### Database Not Found
```bash
# Check PostgreSQL connection
psql -h localhost -U portfolio_user -d portfolio_db

# Verify database exists
psql -U postgres -l

# Run migrations
python manage.py migrate --verbosity 2
```

### Services Return 404
```bash
# Check services in database
python manage.py shell
from services.models import Service
Service.objects.all()

# Seed initial data
python manage.py create_default_services
```

---

## 📝 DEPLOYMENT CHECKLIST (Quick Version)

```bash
# 1. Prepare environment
cp .env.example .env
# Edit .env with production values

# 2. Run migrations
python manage.py migrate

# 3. Seed data
python manage.py create_default_services

# 4. Collect static files
python manage.py collectstatic --noinput

# 5. Run security checks
python manage.py check --deploy

# 6. Test locally (if applicable)
python manage.py runserver

# 7. Deploy (method depends on your choice)
# Docker: docker-compose up -d
# Heroku: git push heroku main
# Server: git pull && supervisorctl restart portfolio

# 8. Verify deployment
curl https://yourdomain.com/services/data-analytics/

# 9. Monitor logs
# Docker: docker-compose logs -f
# Server: sudo supervisorctl tail portfolio
```

---

## 🎓 BEST PRACTICES

### Security
- ✅ Never commit `.env` file
- ✅ Use strong passwords (20+ characters)
- ✅ Regularly update dependencies
- ✅ Use HTTPS everywhere
- ✅ Keep Django and packages updated

### Performance
- ✅ Use database connection pooling
- ✅ Enable caching (Redis recommended)
- ✅ Compress static files (whitenoise handles this)
- ✅ Use a CDN for static/media files
- ✅ Monitor and optimize slow queries

### Reliability
- ✅ Set up automated backups
- ✅ Use health checks
- ✅ Implement error monitoring
- ✅ Keep database backups in separate location
- ✅ Have a rollback plan

### Maintainability
- ✅ Use consistent formatting
- ✅ Keep comprehensive logs
- ✅ Document customizations
- ✅ Use version control properly
- ✅ Test changes before deploying

---

## 📞 SUPPORT

For issues:
1. Check the Troubleshooting section
2. Review Django documentation
3. Check server logs
4. Run `python manage.py check --deploy`

---

**Ready to deploy!** 🚀

Follow the checklist above, choose your deployment method, and your portfolio website will be live!
