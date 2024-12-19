from themer.components.base import (
    AbstractBaseComponent,
    DomPropertiesMixin,
    TextComponentMixin
)

from django_components import (
    register
)


class LinkComponentMixin:
    def update_context(
        self,
        href='#'
    ) -> dict:
        return {
            'href': href
        }    

class IconComponentMixin:
    def update_context(
        self,
        icon='report'
    ) -> dict:
        return {
            'icon': icon,
        }


@register('button')
class Button(
    TextComponentMixin,
    IconComponentMixin,
    DomPropertiesMixin,
    AbstractBaseComponent
):
    template_name = 'button.html'


@register('link')
class Link(
    LinkComponentMixin,
    TextComponentMixin,
    DomPropertiesMixin,
    AbstractBaseComponent,
):
    template_name = 'link.html'


@register('link_button')
class LinkButton(
    LinkComponentMixin,
    TextComponentMixin,
    IconComponentMixin,
    DomPropertiesMixin,
    AbstractBaseComponent
):
    template_name = 'link_button.html'

@register('link_tile')
class LinkTile(
    LinkComponentMixin,
    IconComponentMixin,
    TextComponentMixin,
    DomPropertiesMixin,
    AbstractBaseComponent
):
    template_name = 'link_tile.html'