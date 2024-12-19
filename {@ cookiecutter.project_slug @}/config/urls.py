from django.contrib import admin
from django.urls import (
    path,
    include
)
from django.conf.urls.static import (
    static
)

from django.conf import (
    settings
)

import djp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__reload__', include('django_browser_reload.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('django_components.urls')),
    path('', include('public.urls'), name='public'),
    path('', include('app.urls'), name='app'),
] + static(
    getattr(settings, 'MEDIA_URL'),
    document_root=getattr(settings, 'MEDIA_ROOT')
) + djp.urlpatterns()