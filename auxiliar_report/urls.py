from django.conf.urls import include, url
from .views import AuxiliarReportImportView


urlpatterns = [
    url(r'^import/', AuxiliarReportImportView.as_view()),
]