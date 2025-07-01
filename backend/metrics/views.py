from django.shortcuts import render, HttpResponse
from rest_framework.reverse import reverse
from django.core.serializers.json import DjangoJSONEncoder
import json


from rest_framework import viewsets
from .models import Metric
from .serializers import MetricSerializer

# Create your views here.
def home(request):
    return HttpResponse(f"API is running. This is a homepage {request.method}")


class MetricViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all().order_by('-timestamp')
    serializer_class = MetricSerializer

def dashboard(request):
    host = request.GET.get('host')  # Get ?host=XYZ from URL

    queryset = Metric.objects.all().order_by('-timestamp')
    if host:
        queryset = queryset.filter(host=host)

    metrics = list(queryset[:50][::-1])  # Chronological

    metric_list = [
        {
            'timestamp': m.timestamp.strftime("%H:%M:%S"),
            'cpu_usage': m.cpu_usage,
            'ram_usage': m.ram_usage,
            'disk_usage': m.disk_usage,
            'gpu_usage': m.gpu_usage or 0
        }
        for m in metrics
    ]

    context = {
        'metrics': metric_list,
        'metrics_json': json.dumps(metric_list, cls=DjangoJSONEncoder),
        'selected_host': host,
        'hosts': Metric.objects.values_list('host', flat=True).distinct()
    }
    return render(request, 'metrics/dashboard.html', context)
