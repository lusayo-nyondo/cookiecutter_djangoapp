from django_components import (
    Component,
    register
)

from themer.components.base import (
    AbstractBaseComponent,
    DomPropertiesMixin
)

@register('container')
class Container(
    DomPropertiesMixin,
    AbstractBaseComponent
):
    template_name = 'container.html'


@register('section')
class Section(
    DomPropertiesMixin,
    AbstractBaseComponent
):
    template_name = 'section.html'


class CardComponentMixin:
    def update_context(
        self,
        hide_title=False,
        hide_footer=False
    ):
        return {
            'hide_title': hide_title,
            'hide_footer': hide_footer,
        }


@register('card')
class Card(
    CardComponentMixin,
    DomPropertiesMixin,
    AbstractBaseComponent
):
    template_name = 'card.html'
    
