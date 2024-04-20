from django.db import models

# Create your models here.
class Ai_analysis_log(models.Model):
    image_path = models.CharField(max_length=255, null=True, default=None)
    success = models.BooleanField(null=False)
    message = models.CharField(max_length=255, null=True, default=None)
    class_name = models.IntegerField(null=True, default=None)
    confidence = models.DecimalField(max_digits=5, decimal_places=4, null=True, default=None)
    request_timestamp = models.DateTimeField(null=True, default=None)
    response_timestamp = models.DateTimeField(null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ai_analysis_logs'
    
    def __str__(self):
        return self.image_path
