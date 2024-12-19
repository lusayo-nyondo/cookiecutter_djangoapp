from .settings import (
    get_themer_settings
)

def themer_settings(request):
    all_settings = get_themer_settings()
    
    # Filter out settings relevant for template context processing:
    return {
        'themer_settings': {
            'SITE_TITLE': all_settings['SITE_TITLE'],
            'SITE_URL': all_settings['SITE_URL'],
            'SITE_LOGO': all_settings['SITE_LOGO']
        }
    }
