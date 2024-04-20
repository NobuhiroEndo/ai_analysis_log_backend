from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import AiAnalysisLogsCreateAPIView

router = routers.DefaultRouter()
router.register('list', AiAnalysisLogsCreateAPIView)

urlpatterns = [
    path('create/', AiAnalysisLogsCreateAPIView.as_view(), name='ai_analysis_logs_create'),
]