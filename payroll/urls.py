from django.conf.urls import include, url
from .views import PayrollView, PayrollDayView, PayRollSaveAjaxView, PayrollWeekView


urlpatterns = [
    url(r'^paid/', PayrollView.as_view()),
    url(r'^day/', PayrollDayView.as_view()),
    url(r'^save/', PayRollSaveAjaxView.as_view()),
    url(r'^week/', PayrollWeekView.as_view()),
]
