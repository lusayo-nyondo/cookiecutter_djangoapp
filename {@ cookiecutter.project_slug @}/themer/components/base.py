from abc import abstractmethod
from typing import Any, Dict
import inspect

from django_components import Component

import uuid

class AlpinePropertiesMixin:
    pass

class HtmxPropertiesMixin:
    pass

class TextComponentMixin:
    def update_context(
        self,
        text=''
    ) -> dict:
        return {
            'text': text
        }

class DomPropertiesMixin:
    def update_context(
        self,
        id=''
    ) -> dict: 
        if id == '':
            id = str(uuid.uuid4())
        
        return {
            'id': id,
        }


class AbstractBaseComponent(Component):
    def get_context_updates(self, **context) -> dict:
        context_updates: Dict[str, Any] = {}
        handled_arguments: set = set()
        
        for cls in inspect.getmro(self.__class__):
            if hasattr(cls, 'update_context'):
                method = getattr(cls, 'update_context')
                
                if callable(method) and method != AbstractBaseComponent.update_context:
                    # Get parameter names of the update_context method
                    param_names = inspect.signature(method).parameters.keys()
                    handled_arguments.update(param_names)
                    
                    # Filter context to match the parameters of the current method
                    filtered_context = {key: context[key] for key in param_names if key in context}
                    
                    # Call the mixin's update_context with the filtered context
                    context_update = method(self, **filtered_context)
                    context_updates.update(context_update)
        
        unhandled_arguments = set(context.keys()) - handled_arguments
        
        if unhandled_arguments:
            raise ValueError(f"Unhandled arguments: {', '.join(unhandled_arguments)}")
        
        return context_updates
                
    def get_context_data(self, **context) -> dict:
        return self.get_context_updates(**context)
    
    @abstractmethod
    def update_context(self, *args: Any, **context: Any) -> dict:
        pass
