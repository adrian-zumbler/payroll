from django.conf.urls import include, url
from .views import ScheduleReportImportView


urlpatterns = [
    url(r'^import/', ScheduleReportImportView.as_view()),
]