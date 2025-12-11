# System Architecture

## Overview

This is a Django-based barrister website template with integrated CMS capabilities and an AI-powered intake system.

## Core Components

### Django Application Structure

- **core/**: Django project settings and root URL configuration
- **pages/**: Main application containing all models, views, forms, and URLs
- **Templates/**: HTML templates using Bootstrap 5
  - `base.html`: Base template with navigation and footer
  - `SitePages/`: Individual page templates
- **static/**: CSS, JavaScript, and images

### Data Models

#### Content Management

- **SitePage**: CMS pages (About, Privacy, Terms)
- **HomepageSettings**: Singleton for homepage hero content
- **PracticeArea**: Practice area listings and detail pages
- **BlogPost**: Blog/insights articles
- **CaseStudy**: Case study showcases
- **Lead**: Contact form submissions

#### Booking System

- **Booking**: Calendly webhook integration for consultation bookings
- **AvailabilitySlot**: (If custom booking implemented) Time slot management
- **BookingSubmission**: (If custom booking implemented) Booking form submissions

#### AI Intake System (PHASE 1)

- **IntakeSession**: Captures initial client enquiries through a structured intake form
  - Fields:
    - `uuid`: Unique identifier for each intake session
    - `name`: Optional client name
    - `email`: Optional client email
    - `raw_text`: Required free-text description of the legal matter
    - `structured_output`: JSONField for AI-processed data (PHASE 2+)
    - `recommended_slot_type`: AI recommendation for consultation type (PHASE 2+)
    - `is_suitable`: AI suitability assessment (PHASE 2+)
    - `created_at`: Timestamp

### Intake Flow

**PHASE 1 Implementation (Current):**

1. **Public Intake Form** (`/intake/`)
   - User optionally provides name and email
   - User describes their matter in free-text format
   - Form validates and saves to IntakeSession model
   - No AI processing occurs yet

2. **Thank You Page** (`/intake/thank-you/<uuid>/`)
   - Displays confirmation
   - Shows what was submitted
   - Provides link to booking page
   - Shows reference UUID

3. **Owner Review** (`/owner/intake/`)
   - Staff users can view all intake sessions
   - Read-only table view with:
     - Date/time received
     - Contact information
     - Matter description preview
     - Full text in modal popup
   - No filtering or management features yet

**Future Phases:**

- **PHASE 2**: AI Processing
  - LLM analysis of raw_text to generate structured_output
  - Risk assessment and suitability determination
  - Automatic slot type recommendation
  - Filtering unsuitable enquiries

- **PHASE 3**: Integration & Automation
  - Link intake sessions to booking slots
  - Auto-populate booking forms with intake data
  - Email notifications
  - Advanced owner management (edit, delete, notes)

### Authentication

- **Owner Area**: Protected by `@login_required` and `@user_passes_test(is_staff_user)`
- **Public Pages**: No authentication required
- **Login URL**: Configurable in `core/urls.py` (default: `/site-access-dk2847/`)

### AI Assistant (Optional)

- **Endpoint**: `/api/assist/`
- **Purpose**: Provides general information via chat widget
- **Constraints**: Never provides legal advice, configured with safety guardrails
- **Backend**: Configurable LLM (DeepSeek, OpenAI, or compatible)

## Configuration

All barrister-specific information is managed through environment variables:

- `SITE_NAME`
- `BARRISTER_NAME`
- `BARRISTER_EMAIL`
- `BARRISTER_PHONE`
- `CHAMBERS_ADDRESS_LINE1/2`
- etc.

See `.env.example` for full list.

## Security

- `DEBUG=False` in production
- `ALLOWED_HOSTS` properly configured
- Strong `SECRET_KEY` (50+ characters)
- HTTPS enforced in production (via Render/hosting platform)
- Owner login URL obscured
- CSRF protection on all forms

## Deployment

- Designed for deployment on Render.com
- WhiteNoise for static file serving
- SQLite for development, PostgreSQL recommended for production
- See `DEPLOYMENT.md` for detailed instructions
