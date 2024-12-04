from .exceptions import (
    ThemerSettingKeyError
)

def get_default(setting_name):
    match(setting_name):
        case 'LOGO_STATIC_URL':
            return 'themer/assets/logo.png'
        case _:
            raise ThemerSettingKeyError(f'Themer default setting not found for key: { setting_name }')

def get_setting(dictionary, setting_name):
    try:
        value = dictionary[setting_name]
    except:
        value = get_default(setting_name)
    
    return value

def get_themer_settings():
    try:
        from config.settings.base import (
            THEMER
        )
        
        logo_static_url = get_setting(THEMER, 'LOGO_STATIC_URL')
        
    except:
        # No themer found in settings. Using defaults:
        logo_static_url = get_default('LOGO_STATIC_URL')
    
    return {
        'themer_settings': {
            'LOGO_STATIC_URL': logo_static_url,
        }
    }
