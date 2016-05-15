from django.conf.urls import patterns, url
from .views import home


urlpatterns = patterns('',
    # ex: /language/
    # url(r'^$', index),

    url(r'^$', home),

)
