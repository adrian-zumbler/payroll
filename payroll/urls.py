from django.conf.urls import include, url
from .views import PayrollView


urlpatterns = [
    url(r'^paid/', PayrollView.as_view()),
]