from django_components import (
    Component,
    register
)

@register("table")
class Table(Component):
    template_name = 'table.html'
    
    def get_context_data(self, table_data):
        return {
            "table": {
                "headers": ["col 1", "col 2"],
                "rows": [
                    ["a", "b"],
                    ["c", "d"],
                ]
            }
        }