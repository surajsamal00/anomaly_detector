from django.shortcuts import render,HttpResponse
from rest_framework.reverse import reverse

from rest_framework import viewsets
from .models import Metric
from .serializers import MetricSerializer

# Create your views here.
def home(request):
    return HttpResponse(f"API is running. This is a homepage {request.method}")


class MetricViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all().order_by('-timestamp')
    serializer_class = MetricSerializer