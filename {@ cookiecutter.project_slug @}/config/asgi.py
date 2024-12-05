import os, djp
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')

application = djp.asgi_wrapper(get_asgi_application())
