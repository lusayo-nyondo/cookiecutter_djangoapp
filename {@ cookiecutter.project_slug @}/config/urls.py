import djp
from django.contrib import admin
from django.urls import (
    path,
    include
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__reload__', include('django_browser_reload.urls')),
    path('accounts/', include('allauth.urls')),
    path("", include("django_components.urls")),
    path('', include('public.urls'), name='public'),
    path('', include('app.urls'), name='app'),
] + djp.urlpatterns()