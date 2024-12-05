import json
from datetime import datetime
from django.template import Library
from django.urls import (
    reverse
)

register = Library()

@register.simple_tag(
    takes_context=True
)
def is_current_page_child_of(
    context,
    parent_url: str,
    is_view: bool=True,
    exact_match=False
):
    current_path = context.request.path
    result = True
    
    if is_view:
        parent_url = reverse(parent_url)

        if parent_url.endswith('/'):
            parent_url = parent_url[:-1]
        
        if current_path.endswith('/'):
            current_path = current_path[:-1]

    if exact_match:
        return parent_url == current_path
    else:        
        parent_url_slices = parent_url.split('/')
        current_path_slices = current_path.split('/')
        
        if len(parent_url_slices) > len(current_path_slices):
            result = False
        else:
            for i in range(len(parent_url_slices)):
                parent_slice = parent_url_slices[i]
                current_path_slice = current_path_slices[i]
                
                if parent_slice != current_path_slice:
                    result = False
                    break

    return result

@register.simple_tag
def negate(boolean):
    return (not boolean)

@register.simple_tag
def set_var(var):
    return var

@register.filter(name='get_item')
def get_dict_item(dictionary, key):
    return dictionary.get(key)

@register.filter(name="dict_to_json")
def convert_dict_to_json(dictionary):
    data = json.dumps(dictionary)
    return data

@register.filter(
    name="convert_json_to_dict"
)
def convert_json_to_dict(value):
    obj = json.loads(value)
    return obj


@register.filter(
    name="format_timestamp"
)
def format_timestamp(value):
    time = datetime.fromtimestamp(value)
    return time.strftime("%d/%m/%Y - %H:%M:%S")
