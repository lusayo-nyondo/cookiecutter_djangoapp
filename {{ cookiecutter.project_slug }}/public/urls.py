from django.urls import (
    path
)

from .views import (
    index
)

app_name = 'public'
urlpatterns = [
    path('', index, name='index')    
]
