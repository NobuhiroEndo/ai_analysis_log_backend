from rest_framework import generics
from .models import Ai_analysis_log
from .serializers import AiAnalysisLogSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class AiAnalysisLogsCreateAPIView(generics.CreateAPIView):
    queryset = Ai_analysis_log.objects.all()
    serializer_class = AiAnalysisLogSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)