# Customization Guide

This guide walks you through customizing the barrister website template for your practice.

## Table of Contents

1. [Basic Configuration](#basic-configuration)
2. [Visual Customization](#visual-customization)
3. [Content Management](#content-management)
4. [Adding Your Photo](#adding-your-photo)
5. [Email Configuration](#email-configuration)
6. [AI Assistant Setup](#ai-assistant-setup-optional)
7. [Security Hardening](#security-hardening)

---

## Basic Configuration

### Step 1: Environment Variables

The `.env` file controls all site-specific information. This is the **primary** place to customize your site.

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` with your details:

```env
# Your site name (appears in navbar, page titles, etc.)
SITE_NAME=Jane Smith BL

# Your name (used in content and AI assistant)
BARRISTER_NAME=Jane Smith

# Contact details (appear in header, footer, contact page)
BARRISTER_EMAIL=jane.smith@lawlibrary.ie
BARRISTER_PHONE=01 234 5678
BARRISTER_MOBILE=086 123 4567

# Chambers information (footer and contact page)
CHAMBERS_ADDRESS_LINE1=Law Library, Four Courts
CHAMBERS_ADDRESS_LINE2=Dublin 7, Ireland
CHAMBERS_DX=DX 301175

# Professional details
YEAR_CALLED=2018
PRACTICE_AREAS_SHORT=Commercial, Employment & Regulatory Law
CIRCUITS=Dublin, Eastern & Midland Circuits
QUALIFICATIONS=LLB (Hons), BCL

# Footer biography (one-sentence bio for footer)
BARRISTER_BIO_FOOTER=Junior Counsel specialising in commercial and employment matters
```

3. **Important**: These values are used throughout the site automatically. You don't need to edit templates directly.

### Step 2: Change Owner Login URL

For security, change the owner dashboard login URL:

1. Open `core/urls.py`
2. Find this line:
   ```python
   path("site-access-dk2847/", auth_views.LoginView.as_view(...
   ```
3. Change `site-access-dk2847` to something unique and secure
4. Remember your new URL - you'll use it to access the dashboard

---

## Visual Customization

### Colors and Styling

The template uses a professional navy theme. To customize colors:

1. Open `static/css/site.css`
2. Find the `:root` section at the top:
   ```css
   :root {
     --primary: #2c5aa0;      /* Main blue */
     --primary-dark: #1e3a5f;  /* Darker blue for hovers */
     --text-light: #e8eef7;    /* Light text on dark */
     /* ... more colors ... */
   }
   ```
3. Adjust color values to match your brand
4. Run `python manage.py collectstatic` to apply changes

### Logo and Branding

The site uses text-based branding by default. To add a logo:

1. Add your logo image to `static/img/logo.png`
2. Edit `Templates/base.html`, find the navbar-brand section:
   ```html
   <a class="navbar-brand" href="/">
     <img src="{% static 'img/logo.png' %}" alt="{{ SITE_NAME }}" height="40">
   </a>
   ```

---

## Content Management

### Homepage

1. Log in to Owner Dashboard (your custom URL from Step 2)
2. Click "Edit Homepage"
3. Customize:
   - Hero heading
   - Hero subheading
   - Featured sections

### About Page

**Option 1: Edit via Dashboard** (Recommended)
1. Owner Dashboard → "Manage Site Pages"
2. Click "About"
3. Edit the rich text content
4. Save

**Option 2: Edit Template File**
1. Open `Templates/SitePages/about.html`
2. Modify the fallback content in the `{% else %}` block
3. This content is used if no database content exists

### Practice Areas

1. Owner Dashboard → "Manage Practice Areas"
2. Add your practice areas:
   - Name (e.g., "Employment Law")
   - Short summary (1-2 sentences)
   - Detailed description (full HTML content)
   - Order (display order on site)

### Blog Posts

1. Owner Dashboard → "Manage Blog Posts"
2. Click "Create Blog Post"
3. Fill in:
   - Title
   - Summary (shown on listing page)
   - Full body content (rich text editor)
   - Publish checkbox
   - Published date
4. Save

### Case Studies

1. Owner Dashboard → "Manage Case Studies"
2. Click "Create Case Study"
3. Fill in:
   - Title
   - Summary
   - Full body content
   - Outcome
   - Date of case
   - Associated practice areas
   - Publish checkbox

### Sample Content

To populate the site with example content:

```bash
python manage.py shell < populate_sample_content.py
```

This creates sample:
- Privacy Policy
- Terms of Use
- About page
- 3 practice areas
- 3 blog posts
- 3 case studies

**Remember**: This is placeholder content. Customize it to reflect your actual practice.

---

## Adding Your Photo

### Headshot/Portrait

1. Prepare your photo:
   - Professional headshot
   - Square aspect ratio (e.g., 800x800px)
   - JPG or PNG format
   - Under 500KB for fast loading

2. Add to project:
   - Save as `static/img/headshot.jpg`
   - Or use a different name and update templates

3. The photo appears on:
   - Homepage (hero card)
   - About page (sidebar)

4. If using a different filename, update:
   - `Templates/SitePages/home.html` (line ~31)
   - `Templates/SitePages/about.html` (line ~19)

---

## Email Configuration

The contact form sends emails. Configure SMTP settings:

### Development (Console Email)

Already configured in `core/settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Emails will print to the console/terminal.

### Production (Real Email)

Add to `.env`:
```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your.email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your.email@gmail.com
```

And update `core/settings.py`:
```python
if not DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
    EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
    EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
```

**Gmail Note**: Use an App Password, not your regular Gmail password. See: https://support.google.com/accounts/answer/185833

---

## AI Assistant Setup (Optional)

The AI assistant provides a chat widget on your site that can answer general questions.

### Requirements

- LLM API key (DeepSeek, OpenAI, or compatible endpoint)
- Basic understanding of API configuration

### Setup Steps

1. Get an API key:
   - **DeepSeek** (recommended, cost-effective): https://platform.deepseek.com/
   - **OpenAI**: https://platform.openai.com/
   - Or use any OpenAI-compatible API

2. Add to `.env`:
   ```env
   LLM_BASE_URL=https://api.deepseek.com
   LLM_API_KEY=your-api-key-here
   LLM_MODEL=deepseek-chat
   ASSISTANT_ENABLED=1
   ```

3. The assistant is configured to:
   - Never provide legal advice
   - Direct users to book consultations
   - Provide general information about your practice
   - Include internal links to your pages

4. Test locally:
   - Run development server
   - Click the chat icon in bottom-right
   - Ask test questions

### Customizing Assistant Behavior

Edit the system prompt in `pages/views.py` (line ~383):

```python
SYSTEM_PROMPT = f"""You are a website assistant for {settings.BARRISTER_NAME}.

RULES:
- Provide general, high-level information only. Do NOT give legal advice.
- If the user asks for case-specific guidance, politely decline and suggest booking a consultation.
# ... customize rules as needed ...
"""
```

### Disabling the Assistant

Set in `.env`:
```env
ASSISTANT_ENABLED=0
```

Or remove the LLM configuration entirely.

---

## Security Hardening

### Before Deployment

1. **Generate Strong SECRET_KEY**:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
   Add to production `.env`:
   ```env
   SECRET_KEY=your-super-long-random-secret-key-here
   ```

2. **Set DEBUG=False**:
   ```env
   DEBUG=False
   ```

3. **Configure ALLOWED_HOSTS**:
   ```env
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   ```

4. **Change Owner Login URL** (mentioned earlier):
   - Edit `core/urls.py`
   - Use a random, hard-to-guess path

5. **Update .gitignore**:
   Ensure `.env` is NOT committed to Git:
   ```
   .env
   db.sqlite3
   ```

6. **Create Strong Superuser Password**:
   ```bash
   python manage.py createsuperuser
   ```
   Use a password manager to generate a strong password.

### Additional Security

- **HTTPS**: Render.com provides this automatically
- **Database**: Consider PostgreSQL for production (SQLite resets on deploy)
- **Media Files**: Use cloud storage (S3, Cloudflare R2) for uploaded images
- **Rate Limiting**: Consider adding django-ratelimit for contact form
- **Security Headers**: Already configured in `core/settings.py` for production

---

## Common Customizations

### Change Footer Copyright

Edit `.env`:
```env
SITE_NAME=Your Name BL
```

The footer automatically uses `{{ SITE_NAME }}`.

### Add Social Media Links

Edit `Templates/base.html`, footer section (~line 100):
```html
<div class="social-links">
  <a href="https://linkedin.com/in/yourprofile"><i class="bi bi-linkedin"></i></a>
  <a href="https://twitter.com/yourhandle"><i class="bi bi-twitter"></i></a>
</div>
```

### Change Booking Flow

The custom booking system can be customized:

1. **Slot Types**: Edit `pages/models.py`, `AvailabilitySlot.SLOT_TYPE_CHOICES`
2. **Payment Integration**: Update `Templates/SitePages/booking_success.html`
3. **Booking Form Fields**: Edit `pages/forms.py`, `BookingSubmissionForm`

### Remove AI Assistant Widget

If you don't want the assistant at all:

1. Remove from `Templates/base.html`:
   ```django
   {# {% include 'includes/assistant.html' %} #}
   ```

---

## Troubleshooting

### Changes Not Showing?

1. Restart development server
2. Clear browser cache (Ctrl+Shift+R)
3. Run `python manage.py collectstatic` for static file changes
4. Check `.env` file is in project root

### Owner Dashboard Not Accessible?

1. Verify you created a superuser: `python manage.py createsuperuser`
2. Check the login URL matches `core/urls.py`
3. Ensure migrations are applied: `python manage.py migrate`

### Email Not Sending?

1. Check console output (development mode)
2. Verify SMTP settings in production
3. Check email provider allows SMTP (Gmail requires App Passwords)

### Static Files Not Loading?

1. Run `python manage.py collectstatic`
2. Check `STATIC_ROOT` in `core/settings.py`
3. Ensure WhiteNoise middleware is enabled

---

## Next Steps

1. ✅ Complete basic configuration (`.env`)
2. ✅ Add your photo
3. ✅ Populate content via Owner Dashboard
4. ✅ Customize colors/styling
5. ✅ Test locally
6. ✅ Deploy to Render (see `DEPLOYMENT.md`)
7. ✅ Add custom domain
8. ✅ Configure email
9. ✅ Set up AI assistant (optional)

---

**Need help?** Check `README.md` for additional resources or see `DEPLOYMENT.md` for deployment instructions.
