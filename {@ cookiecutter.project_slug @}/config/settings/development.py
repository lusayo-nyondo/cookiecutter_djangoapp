from .base import *

MIDDLEWARE.append(
    'config.middleware.no_cache_middleware',
)