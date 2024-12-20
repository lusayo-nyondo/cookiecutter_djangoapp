from .settings import (
    get_themer_settings
)

def themer_context(request):
    themer_settings = get_themer_settings()
    
    return {
        'themer_settings': {
            'SITE_TITLE': themer_settings['SITE_TITLE'],
            'SITE_URL': themer_settings['SITE_URL'],
            'SITE_LOGO': themer_settings['SITE_LOGO']
        }
    }
