from django.conf.urls import include, url
from .views import OccupancyImportView


urlpatterns = [
    url(r'^import/', OccupancyImportView.as_view()),
]