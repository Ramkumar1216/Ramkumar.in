# Customization Guide

How to customize the portfolio website for your brand

## 🎨 Website Title & Colors

### Change Website Title

**File**: `portfolio_project/settings.py`

Change line in admin site configuration:
```python
admin.site.site_header = "Your Name Portfolio Admin"
admin.site.site_title = "Your Name"
```

Also update `base.html`:
```html
<title>{% block title %}Your Name - Services Offered{% endblock %}</title>
```

### Change Brand Colors

**File**: `templates/base.html`

Find this CSS and update colors:
```css
.gradient-bg {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

Change the hex colors:
- `#667eea` → Your primary color
- `#764ba2` → Your secondary color

Popular color combinations:
- Tech Blue: `#2563eb` to `#0ea5e9`
- Business Green: `#047857` to `#059669`
- Creative Orange: `#ea580c` to `#f97316`
- Modern Purple: `#7c3aed` to `#a855f7`

## 👤 Personal Information

### Update Your Name

Search and replace "Ramkumar" with your name in:
1. `templates/base.html` - Logo/navbar
2. `templates/core/home.html` - Hero section
3. `templates/core/about.html` - About page
4. `portfolio_project/settings.py` - Admin title

### Update Contact Information

**WhatsApp Number**:
- Search for `wa.me/919876543210` in all templates
- Replace with your WhatsApp number (include country code, no + symbol)

**Email Address**:
- Look for `ramkumar@example.com` in templates
- Replace with your email

**Social Media Links**:
In `templates/base.html` footer:
```html
<a href="https://linkedin.com/in/YOUR_LINKEDIN" target="_blank">LinkedIn</a>
<a href="https://github.com/YOUR_GITHUB" target="_blank">GitHub</a>
<a href="https://instagram.com/YOUR_INSTAGRAM" target="_blank">Instagram</a>
```

## 📝 Text Content Updates

### Hero Section (Home Page)

**File**: `templates/core/home.html`

```html
<h1 class="text-5xl md:text-6xl font-bold mb-6 leading-tight">
    Hi, I'm <span class="gradient-bg">Your Name</span> 🚀
</h1>
<p class="text-xl text-gray-400 mb-8 leading-relaxed">
    Your tagline - e.g., "Full-Stack Developer helping startups scale"
</p>
```

### About Page Bio

**File**: `templates/core/about.html`

Update the story section with your journey:
```html
<p class="text-gray-400 mb-4 leading-relaxed">
    Your story here...
</p>
```

### Footer Text

**File**: `templates/base.html`

Find footer section and update company description:
```html
<p class="text-gray-400 text-sm">
    Your company description and what you do...
</p>
```

## 🖼️ Images

### Add Project Images

1. Prepare your project screenshots/images
2. Go to Admin Panel → Projects → Add Project
3. Upload image in "Image" field
4. Save

**Recommended Image Size**: 1200x600px (landscape)

### Add Logo (Optional)

1. Create a logo image
2. Save to `static/images/logo.png`
3. Update `base.html` to reference it:
```html
<img src="{% static 'images/logo.png' %}" alt="Logo" class="h-8">
```

## 🎯 Services Customization

### Update Service Offerings

Go to Admin Panel → Services

Remove services you don't offer and adjust features/pricing:

**Example - Data Analytics**:
- Title: "Data Analytics"
- Price: "₹999+"
- Features: "Custom dashboards, Data analysis, Weekly reports, Expert consultation"

**Example - Web Development**:
- Title: "Web Development"
- Price: "₹1999+"
- Features: "Responsive design, SEO optimization, CMS integration, Mobile friendly"

### Change Service Icons

Services use emoji icons. Pop in any emoji:
- 📊 - Analytics
- 💻 - Development
- 🎯 - Marketing
- 📱 - Mobile
- 🔍 - SEO
- 📈 - Growth

## 📱 Mobile Navigation

The website auto-adjusts for mobile. To customize:

**File**: `templates/base.html`

Mobile menu HTML is here:
```html
<!-- Mobile Menu -->
<div id="mobile-menu" class="hidden md:hidden bg-gray-900 bg-opacity-95">
    <!-- Update links here -->
</div>
```

## 🔧 Settings Customization

**File**: `portfolio_project/settings.py`

### Change Admin Title

```python
admin.site.site_header = "Your Portfolio Admin"
```

### Add Allowed Hosts (For Production)

```python
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

### Enable Email (Optional)

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

## 🎨 Font Customization

Currently using "Poppins" font. To change:

**File**: `templates/base.html`

```html
<link href="https://fonts.googleapis.com/css2?family=YourFontName:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

Then update CSS:
```css
* {
    font-family: 'YourFontName', sans-serif;
}
```

Popular alternatives:
- "Inter" - Clean, modern
- "Playfair Display" - Elegant, serif
- "Montserrat" - Bold, geometric
- "Raleway" - Light, minimal

## 📧 Email Notifications

### Enable Contact Form Emails

Update `contact/views.py`:

```python
from django.core.mail import send_mail

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            # Send email on contact submission
            send_mail(
                f'New Message from {contact.name}',
                contact.message,
                contact.email,
                ['your-email@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Message sent successfully!')
            return redirect('contact:contact')
```

## 🌙 Dark Theme Toggle (Advanced)

To add light/dark mode toggle, update `base.html` and add:

```html
<button onclick="toggleDarkMode()" class="text-gray-300">
    🌙 / ☀️
</button>

<script>
function toggleDarkMode() {
    document.body.classList.toggle('light-mode');
}
</script>
```

## 🔍 SEO Optimization

### Add Meta Descriptions

In `base.html`:
```html
<meta name="description" content="Your website description for search engines">
<meta name="keywords" content="keyword1, keyword2, keyword3">
<meta name="author" content="Your Name">
```

### Create Sitemap (Advanced)

Use Django sitemap framework or create manually:
1. Add `django.contrib.sites` to `INSTALLED_APPS`
2. Configure sitemaps in `urls.py`

## 📊 Analytics (Optional)

### Add Google Analytics

In `templates/base.html` before closing `</head>`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-GA-ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR-GA-ID');
</script>
```

Replace `YOUR-GA-ID` with your Google Analytics ID.

## 🚀 Quick Customization Checklist

- [ ] Change your name (search "Ramkumar")
- [ ] Update WhatsApp number
- [ ] Update email address
- [ ] Change website colors
- [ ] Update hero section text
- [ ] Add your services in admin
- [ ] Add your projects in admin
- [ ] Update about page
- [ ] Update footer links
- [ ] Add Google Analytics

---

**Need more help?** Check README.md or contact support!
