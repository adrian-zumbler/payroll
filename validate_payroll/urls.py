from django.conf.urls import include, url
from .views import ValidatePayrollView, ValidatePayrollCreateView


urlpatterns = [
    url(r'^status/', ValidatePayrollView.as_view()),
    url(r'^save/', ValidatePayrollCreateView.as_view()),

]
