from django.conf.urls import url
from .views import PeriodListView


urlpatterns = [
    url(r'^list/',PeriodListView.as_view()),
]
