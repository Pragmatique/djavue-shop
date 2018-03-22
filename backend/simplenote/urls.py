from django.conf.urls import include, url
from django.contrib import admin
from shop.views import index

urlpatterns = [
    url(r'^api/v1/', include('shop.urls')),

    url(r'^admin/', admin.site.urls),

    url(r'^$', index)
]
