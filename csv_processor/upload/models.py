# upload/models.py

from django.db import models

class GeneratedFileLog(models.Model):
    file_type = models.CharField(max_length=100)
    file_name = models.CharField(max_length=255)
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file_type} - {self.file_name} - {self.generated_at}"
