from django.conf.urls import include, url
from . import views
from .views import AgentStatisticsView

urlpatterns = [
    url(r'^export/', views.export,name="export" ),
    url(r'^statistics/',AgentStatisticsView.as_view(),name="statistics"),
]
