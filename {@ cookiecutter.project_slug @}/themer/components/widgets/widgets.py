from themer.components.base import (
    AbstractBaseComponent,
    DomPropertiesMixin,
)

from django_components import (
    register
)

class WidgetComponentMixin:
    def update_context(self,
        label='',
        placeholder='',
        name='',
        has_label=True,
    ):        
        return {
            'has_label': has_label,
            'label': label,
            'placeholder': placeholder,
            'name': name,
        }

@register('text_input')
class TextInput(
    WidgetComponentMixin,
    DomPropertiesMixin,
    AbstractBaseComponent
):
    template_name = 'text_input.html'

@register('select')
class SelectInput(
    WidgetComponentMixin,
    DomPropertiesMixin,
    AbstractBaseComponent
):
    template_name = 'select.html'
    
@register('date_input')
class DateInput(
    WidgetComponentMixin,
    DomPropertiesMixin,
    AbstractBaseComponent
):
    template_name = 'date_input.html'
