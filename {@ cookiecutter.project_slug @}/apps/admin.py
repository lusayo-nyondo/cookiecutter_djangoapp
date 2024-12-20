from typing import (
    List
)
from django.urls import (
    URLPattern,
    path
)
from django.utils.translation import gettext_lazy as _

from unfold.sites import UnfoldAdminSite

from themer.settings import (
    get_themer_settings
)

class AppsAdminSite(UnfoldAdminSite):
    __themer_settings = get_themer_settings()
    
    site_header = _(__themer_settings['SITE_TITLE'])
    site_title = _(__themer_settings['SITE_TITLE'])
    index_title = _(__themer_settings['SITE_TITLE'])

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