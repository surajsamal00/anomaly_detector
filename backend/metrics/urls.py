from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from .views import MetricViewSet

router = DefaultRouter()
router.register(r'metrics', MetricViewSet, basename='metric')


urlpatterns = [
    path('home/', views.home),
    path('',include(router.urls))
]
