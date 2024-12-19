from .exceptions import (
    ThemerSettingKeyError
)

def get_default(setting_name):
    match(setting_name):
        case 'SITE_LOGO':
            return 'themer/assets/logo.png'
        case 'COLOR_PALETTES':
            return {
                "primary": {
                    '50': '#effaff',
                    '100': '#daf3ff',
                    '200': '#beebff',
                    '300': '#91dfff',
                    '400': '#5ecbfc',
                    '500': '#38aff9',
                    '600': '#2293ee',
                    '700': '#1976d2',
                    '800': '#1c63b1',
                    '900': '#1c548c',
                    '950': '#163355',
                }
            }
        case _:
            raise ThemerSettingKeyError(f'Themer default setting not found for key: { setting_name }')

def get_setting(dictionary, setting_name):
    if dictionary:
        try:
            value = dictionary[setting_name]
        except:
            value = get_default(setting_name)
    else:
        value = get_default(setting_name)
    
    return value
    
def get_themer_settings():
    try:
        from config.settings.base import (
            THEMER
        )
        themer = THEMER
    except:
        # No themer found in settings.
        themer = None
    
    site_logo = get_setting(themer, 'SITE_LOGO')
    color_palettes = get_setting(themer, 'COLOR_PALETTES')
    site_title = get_setting(themer, 'SITE_TITLE')
    site_url = get_setting(themer, 'SITE_URL')
    
    return {
        'SITE_LOGO': site_logo,
        'COLOR_PALETTES': color_palettes,
        'SITE_TITLE': site_title,
        'SITE_URL': site_url,
    }
