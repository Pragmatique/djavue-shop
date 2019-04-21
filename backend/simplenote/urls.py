from django.conf.urls import include, url
from django.contrib import admin
from shop.views import index
from accounts.urls import router
from rest_framework.generics import ListCreateAPIView
from rest_framework import routers
import accounts.urls


urlpatterns = [
    url(r'^api/v2/', include(('accounts.urls','accounts'), namespace='auth')),
    url(r'^api/v1/', include('shop.urls', namespace='shop')),

    url(r'^admin/', admin.site.urls),
    url(r'^$', index)
]
