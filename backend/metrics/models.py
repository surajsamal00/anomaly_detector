from django.db import models

# Create your models here.
class Metric(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    cpu_usage = models.FloatField()
    ram_usage = models.FloatField()
    disk_usage = models.FloatField()
    gpu_usage = models.FloatField(null=True, blank=True)
    host = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.host} @ {self.timestamp}"
