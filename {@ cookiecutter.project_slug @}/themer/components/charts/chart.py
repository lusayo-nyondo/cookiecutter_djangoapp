import uuid

from django_components import (
    Component,
    register,
    types
)

from themer.exceptions import (
    ThemerComponentKeyError
)

@register('chart')
class Chart(Component):
    __mode: str = 'bar'
    
    @property
    def mode(self):
        return self.__mode
    
    @mode.setter
    def mode(self, value):
        if value not in [
            'line',
            'box'
        ]: raise ThemerComponentKeyError(
            "Invalid value for Chart component's mode argument: %s",
            value
        )
        
        self.__mode = value

    template_name = 'chart.html'
    
    class Media:
        js = 'chart.js'
    
    def get_context_data(self,
        mode: str='',
        height: int=100,
        width: int=100,
    ):
        chart_id = "my_chart"
        
        if mode:
            self.mode = mode
            
        return {
            'id': chart_id,
            'mode': mode,
            'height': height,
            'width': width,
        }
    