from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

# import required to hook up receivers
from . import receivers


urlpatterns = patterns("",
    url(r"^admin/", include(admin.site.urls)),

    url(r"^account/", include("account.urls")),
    url(r"^profiles/", include("forums.profiles.urls")),
    
    url(r"", include("agora.urls"))
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
