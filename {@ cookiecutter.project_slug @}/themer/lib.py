import os

from django.conf import (
    settings
)

def get_themer_path():
    return os.path.join(
        getattr(settings, 'BASE_DIR'),
        'themer'
    )