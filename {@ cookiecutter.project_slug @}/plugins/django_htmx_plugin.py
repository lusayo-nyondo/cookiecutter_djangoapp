import djp

@djp.hookimpl
def middleware():
    return [
        "django_htmx.middleware.HtmxMiddleware",
    ]
