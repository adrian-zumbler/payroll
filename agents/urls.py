from django.conf.urls import include, url
from . import views
from .views import YesterdayStatistiscsView,TemplateAgentStatistics


urlpatterns = [
    url(r'^yesterdayStatistics/',YesterdayStatistiscsView.as_view(),name="yesterdayStatistics"),
    url(r'^statistics/',TemplateAgentStatistics.as_view(),name="statistics"),
    url(r'^export/', views.export,name="export" ),

]
