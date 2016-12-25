from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
]
