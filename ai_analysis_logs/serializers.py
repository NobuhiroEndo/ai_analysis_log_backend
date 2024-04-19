from rest_framework import serializers
from .models import Ai_analysis_log

class AiAnalysisLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ai_analysis_log
        fields = [
            'id',
            'image_path',
            'success',
            'message',
            'class_name',
            'confidence',
            'request_timestamp',
            'response_timestamp',
            'created_at',
            'updated_at'
        ]