from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import AiAnalysisLogsViewSet

router = routers.DefaultRouter()
router.register('list', AiAnalysisLogsViewSet)

urlpatterns = [
    path('', include(router.urls))
]