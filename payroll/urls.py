from django.conf.urls import include, url
from .views import PayrollView, PayrollDayView, PayRollSaveAjaxView


urlpatterns = [
    url(r'^paid/', PayrollView.as_view()),
    url(r'^day/', PayrollDayView.as_view()),
    url(r'^save/', PayRollSaveAjaxView.as_view()),
]
