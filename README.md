# Barrister Website Template

A professional Django-based website template for barristers, featuring a modern design, content management system, and optional AI assistant.

## Features

- **Content Management System**: Easy-to-use owner dashboard for managing:
  - Practice areas
  - Blog posts
  - Case studies
  - Site pages (About, Privacy, Terms)
  - Homepage content

- **Custom Booking System**:
  - Owner-managed availability slots
  - Public booking flow
  - Booking tracking with payment status
  - Revolut payment integration support

- **Professional Design**:
  - Bootstrap 5 with Premium Legal UI
  - Fully responsive layout
  - Professional navy color scheme
  - Mobile-friendly navigation

- **Optional AI Assistant**:
  - Website chat widget
  - Configurable LLM backend (DeepSeek, OpenAI, etc.)
  - Context-aware responses about your practice

- **Contact Form**: With email notifications

- **Ready for Deployment**:
  - WhiteNoise for static file serving
  - Render.com deployment configuration
  - Environment-based configuration

## Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/yourusername/barrister-template-v1.git
cd barrister-template-v1
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy `.env.example` to `.env` and customize with your details:

```bash
cp .env.example .env
```

Edit `.env` with your information:

```env
SITE_NAME=Your Name BL
BARRISTER_NAME=Your Name
BARRISTER_EMAIL=your.email@example.com
BARRISTER_PHONE=01 XXX XXXX
# ... (see .env.example for all options)
```

See `CUSTOMIZE.md` for detailed configuration instructions.

### 5. Initialize Database

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Populate Sample Content (Optional)

```bash
python manage.py shell < populate_sample_content.py
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` to see your site!

## Customization

For detailed customization instructions, see `CUSTOMIZE.md`.

Key customization areas:
- Site configuration (`.env` file)
- Colors and styling (`static/css/site.css`)
- Practice areas (Owner Dashboard)
- About page content (Owner Dashboard)
- Blog posts and case studies (Owner Dashboard)

## Owner Dashboard

Access the owner dashboard at `http://localhost:8000/site-access-dk2847/`

**IMPORTANT**: Change the login URL in `core/urls.py` before deployment for security.

From the dashboard you can:
- Edit homepage content
- Manage practice areas
- Create and edit blog posts
- Create and edit case studies
- Manage site pages
- Manage availability slots
- View booking submissions

## Deployment

See `DEPLOYMENT.md` for detailed deployment instructions for Render.com.

Quick deployment steps:
1. Generate a strong `SECRET_KEY`
2. Push to GitHub
3. Create Render web service
4. Add environment variables
5. Deploy

## Project Structure

```
barrister-template-v1/
├── core/                  # Django project settings
├── pages/                 # Main app (views, models, forms)
├── Templates/
│   ├── base.html         # Base template
│   └── SitePages/        # Page templates
├── static/
│   ├── css/              # Stylesheets
│   ├── js/               # JavaScript
│   └── img/              # Images
├── .env.example          # Environment variables template
├── requirements.txt      # Python dependencies
├── build.sh              # Render build script
└── manage.py            # Django management script
```

## Configuration System

The template uses a centralized configuration system that pulls barrister-specific information from environment variables. This makes it easy to:

- Deploy the same codebase for different barristers
- Update contact information without touching code
- Maintain separate development and production configurations

All configuration is managed through:
- Environment variables (`.env` file)
- Django settings (`core/settings.py`)
- Context processor (`pages/context_processors.py`)

## Features in Detail

### Custom Booking System

The template includes a fully custom booking system that replaces Calendly:

- **Availability Management**: Create and manage time slots from the Owner Dashboard
- **Public Booking Flow**: Users select date → time slot → submit booking details
- **Payment Integration**: Shows Revolut QR code after booking
- **Booking Tracking**: View all bookings with payment status toggle

### AI Assistant

Optional AI-powered chat widget that can:
- Answer general questions about your practice
- Provide information about practice areas
- Direct users to relevant pages
- Never provide legal advice (configured with safety guardrails)

Requires:
- LLM API key (DeepSeek, OpenAI, or compatible)
- Configuration in `.env` file

### Content Management

Easy content editing through the Owner Dashboard:
- Rich text editor for long-form content
- Image upload support
- Draft/publish workflow
- SEO-friendly URLs

## Support

- Django Documentation: https://docs.djangoproject.com/
- Bootstrap 5 Documentation: https://getbootstrap.com/docs/5.3/
- Render Deployment: https://render.com/docs

## License

This template is provided as-is for use by barristers to create professional websites.

## Acknowledgments

Built with:
- Django 5
- Bootstrap 5
- WhiteNoise
- CKEditor

---

**Need help customizing this template?** See `CUSTOMIZE.md` for step-by-step instructions.

**Ready to deploy?** See `DEPLOYMENT.md` for deployment instructions.
