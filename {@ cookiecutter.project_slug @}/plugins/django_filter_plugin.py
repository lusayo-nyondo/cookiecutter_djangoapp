import djp

@djp.hookimpl
def installed_apps():
    return [
        "django_filters",
    ]
