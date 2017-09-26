# from django.conf.urls import *
#
# from blog.views import *
#
# urlpatterns = [
#     url(r'^$', archive),
#     url(r'^/blog/create/', create_blogpost),
# ]

from django.conf.urls import *
from django.contrib import admin
from blog.views import *
admin.autodiscover()

urlpatterns = (
    url(r'^$', archive),
    url(r'create/', create_blogpost),
)
