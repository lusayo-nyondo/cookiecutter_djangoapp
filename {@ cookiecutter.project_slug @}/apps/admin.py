from typing import (
    List
)
from django.urls import (
    URLPattern,
    path
)
from django.utils.translation import gettext_lazy as _

from unfold.sites import UnfoldAdminSite

class AppsAdminSite(UnfoldAdminSite):
    site_header = _('Courier Management')
    site_title = _('Courier Management')
    index_title = _('Courier Management')

    __extra_urls: list = []
    
    def get_urls(self) -> List[URLPattern]:
        urlpatterns = super().get_urls()
        urlpatterns = self.__extra_urls + urlpatterns
        return urlpatterns
    
    def register_url(self, url, function, **kwargs):
        assert isinstance(url, str)
        assert callable(function)
        
        self.__extra_urls.append(
            path(
                url,
                self.admin_view(function(self)),
                **kwargs
            )
        )
    
admin_site = AppsAdminSite()