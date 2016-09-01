from django.conf.urls import url
from django.contrib import admin

from web.views import index

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
]
