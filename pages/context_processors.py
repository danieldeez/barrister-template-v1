from django.conf import settings

def assistant_enabled(request):
    """Make ASSISTANT_ENABLED available in all templates."""
    return {
        'ASSISTANT_ENABLED': settings.ASSISTANT_ENABLED
    }

def barrister_config(request):
    """
    Provides barrister-specific configuration to all templates.
    These values should be customized in core/settings.py for each deployment.
    """
    return {
        'SITE_NAME': getattr(settings, 'SITE_NAME', '[Your Name] BL'),
        'BARRISTER_NAME': getattr(settings, 'BARRISTER_NAME', '[Your Name]'),
        'BARRISTER_EMAIL': getattr(settings, 'BARRISTER_EMAIL', 'your.email@example.com'),
        'BARRISTER_PHONE': getattr(settings, 'BARRISTER_PHONE', '01 XXX XXXX'),
        'BARRISTER_MOBILE': getattr(settings, 'BARRISTER_MOBILE', '0XX XXX XXXX'),
        'CHAMBERS_ADDRESS_LINE1': getattr(settings, 'CHAMBERS_ADDRESS_LINE1', 'Your Chambers'),
        'CHAMBERS_ADDRESS_LINE2': getattr(settings, 'CHAMBERS_ADDRESS_LINE2', 'Your City, Your Country'),
        'CHAMBERS_DX': getattr(settings, 'CHAMBERS_DX', 'DX XXXXXX'),
        'YEAR_CALLED': getattr(settings, 'YEAR_CALLED', '20XX'),
        'PRACTICE_AREAS_SHORT': getattr(settings, 'PRACTICE_AREAS_SHORT', 'Your practice areas'),
        'BARRISTER_BIO_FOOTER': getattr(settings, 'BARRISTER_BIO_FOOTER', 'Junior Counsel practising at the Bar. Providing focused advice and advocacy.'),
        'CIRCUITS': getattr(settings, 'CIRCUITS', 'Your Circuits'),
        'QUALIFICATIONS': getattr(settings, 'QUALIFICATIONS', 'Your Qualifications'),
    }
