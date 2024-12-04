from .settings import (
    get_themer_settings
)

def themer_settings(request):
    all_settings = get_themer_settings()
    
    # Filter out settings relevant for template context processing:
    return {
        'themer_settings': {
            'LOGO_STATIC_URL': all_settings['LOGO_STATIC_URL']
        }
    }
