from django.template.loader_tags import (
    ExtendsNode
)

"""
    This adds a custom loader tag: {% extends_partial %}.
    
    This tag checks if the incoming request has any HTMX headers.
    
    If it does, it returns the template without applying the {% extends %}.
    If it does not, it first extends then returns the view.
    
    I wasn't sure whether to do this in the view layer or in the template layer,
    so I've opted to do it in the template layer and see how it works.
"""
class ExtendsPartial():
    pass
