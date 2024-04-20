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
        image_path = request.data.get('image_path', '')
        success = request.data['response_from_API']['success']
        message = request.data['response_from_API']['message']
        estimated_data = request.data['response_from_API'].get('estimated_data', {})
        class_value = estimated_data.get('class')
        confidence = estimated_data.get('confidence')
        request_timestamp = request.data['request_timestamp']
        response_timestamp = request.data['response_timestamp']

        instance = Ai_analysis_log(
            image_path=image_path,
            success=success,
            message=message,
            class_name=class_value,
            confidence=confidence,
            request_timestamp=request_timestamp,
            response_timestamp=response_timestamp
        )

        instance.save()

        serializer = self.get_serializer(instance)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)