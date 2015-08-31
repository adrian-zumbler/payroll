from django.conf.urls import include, url
from .views import ValidatePayrollView


urlpatterns = [
    url(r'^', ValidatePayrollView.as_view()),

]
