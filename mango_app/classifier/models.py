from django.db import models
import uuid
import os


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    return f'uploads/{uuid.uuid4().hex}.{ext}'


class ScanHistory(models.Model):
    id = models.AutoField(primary_key=True)
    session_key = models.CharField(max_length=64, blank=True, db_index=True)
    image = models.ImageField(upload_to=upload_to)
    top_disease = models.CharField(max_length=100)
    top_confidence = models.FloatField()
    all_predictions = models.JSONField(default=list)
    is_healthy = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Scan History'
        verbose_name_plural = 'Scan Histories'

    def __str__(self):
        return f"[{self.created_at:%Y-%m-%d %H:%M}] {self.top_disease} ({self.top_confidence:.1f}%)"

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''


class Feedback(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    scan = models.OneToOneField(ScanHistory, on_delete=models.CASCADE, related_name='feedback')
    rating = models.IntegerField(choices=RATING_CHOICES)
    correct_diagnosis = models.BooleanField(null=True, blank=True)
    correct_disease = models.CharField(max_length=100, blank=True)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for scan #{self.scan_id} — {self.rating}★"
