from django.conf.urls import patterns, url
from rest_framework import routers
from .views import home, StudentViewSet


urlpatterns = patterns('',
    # ex: /language/
    # url(r'^$', index),

    url(r'^$', home),
    #url(r'^students/$', StudentsView.as_view()),
    #url(r'^classrooms/$', ClassroomsView.as_view())
)


# router = routers.SimpleRouter()
# router.register(r'students', StudentsView)
# router.register(r'classrooms', ClassroomsView)
# urlpatterns += router.urls