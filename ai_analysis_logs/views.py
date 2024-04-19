from django.shortcuts import render
from .models import Ai_analysis_log
from rest_framework import viewsets
from .serializers import AiAnalysisLogSerializer

# Create your views here.
class AiAnalysisLogsViewSet(viewsets.ModelViewSet):
    queryset = Ai_analysis_log.objects.all()
    serializer_class = AiAnalysisLogSerializer
