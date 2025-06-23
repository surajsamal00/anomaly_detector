from django.contrib import admin
from .models import Metric
# Register your models here.



# admin.site.register(Metric)  #basic way

@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ('host', 'cpu_usage', 'ram_usage')
    list_filter = ('host', 'timestamp')
    search_fields = ('host',)

