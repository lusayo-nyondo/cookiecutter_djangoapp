from django.apps import AppConfig


class OverrideDjangoFormsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'override_django_forms'
