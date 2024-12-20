import os
from pathlib import Path
from django_components import ComponentsSettings
from django.templatetags.static import static
from apps.config import (
    SIDEBAR
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%-@hw*b=(x=hr$lxi%s-wzb98m$!dkn&!l*s#tq)&6b(k+f22d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'
]


# Application definition

INSTALLED_APPS = [
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    "unfold.contrib.simple_history", 
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'allauth',
    'allauth.account',
    
    'django_components',
    
    'django_browser_reload',
    'hook_django_unfold',
    
    'themer',
    'public',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'django_browser_reload.middleware.BrowserReloadMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    "django_components.middleware.ComponentDependencyMiddleware",
]

ROOT_URLCONF = 'config.urls'

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / os.path.join('themer', 'overrides', 'override_django_allauth', 'templates'),
            BASE_DIR / os.path.join('themer', 'overrides', 'override_django_forms', 'templates'),
            
            BASE_DIR / os.path.join('apps', 'hook_django_unfold', 'templates'),
        ],
        # 'APP_DIRS': True, Removed for compatibility with Django Components
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'themer.context_processors.themer_context',
            ],
            'loaders': [(
                'django.template.loaders.cached.Loader', [
                    # Default Django loader
                    'django.template.loaders.filesystem.Loader',
                    # Inluding this is the same as APP_DIRS=True
                    'django.template.loaders.app_directories.Loader',
                    # Components loader
                    'django_components.template_loader.Loader',
                ]
            )],
            'builtins': [
                'django_components.templatetags.component_tags',
                'themer.templatetags.themer_tags',
                'djp.templatetags.djp',
            ]
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = '/public_static/'
STATICFILES_FINDERS = [
    # Default finders
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # Django components
    "django_components.finders.ComponentsFileSystemFinder",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

#{( set auth_method = cookiecutter.account_authentication_method )}
#{( if auth_method == "email" )}
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
#{( elif auth_method == "Username" )}
ACCOUNT_AUTHENTICATION_METHOD = "username"
#{( elif auth_method == "All" )}
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
#{( else )}
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
#{( endif )}

LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/dashboard'

THEMER = {
    'SITE_TITLE': '{@ cookiecutter.project_name @}',
    'SITE_DESCRIPTION': '{@ cookiecutter.description @}',
    'SITE_LOGO': lambda request: static('themer/assets/logo.png'),
    'SITE_ICON': lambda request: static('themer/assets/logo.png'),
    'APPS_DIR': BASE_DIR / 'apps',
    'SITE_URL': '/',
    'APP_URL': '/app',
    'COLOR_PALETTES': {
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
        }, 
    }
}

UNFOLD = {
    "SITE_TITLE": THEMER['SITE_TITLE'],
    "SITE_HEADER": THEMER['SITE_TITLE'],
    "SITE_URL": THEMER['SITE_URL'],
    "SITE_LOGO": THEMER['SITE_LOGO'],
    "SITE_ICON": THEMER['SITE_ICON'],
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/png",
            "href": lambda request: static(THEMER['LOGO_STATIC_URL']),
        },
    ],
    "COLORS": THEMER['COLOR_PALETTES'],
    "SIDEBAR": SIDEBAR,
}

COMPONENTS = ComponentsSettings(
    dirs=[],
    app_dirs=[
        'components',
    ],   
    reload_on_file_change=True
)


MEDIA_ROOT = BASE_DIR / 'public_media'
MEDIA_URL = '/media/'

DJP_PLUGINS_DIR = str(BASE_DIR / 'plugins')
os.environ.setdefault(
    "DJP_PLUGINS_DIR",
    DJP_PLUGINS_DIR
)
import djp # Import DJP Strictly After loading the environment variable so it gets plugins correctly.
djp.settings(globals())
