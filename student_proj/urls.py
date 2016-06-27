from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from students.views import StudentViewSet, home, ClassroomViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'classrooms', ClassroomViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^', include(router.urls)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.autodiscover()
