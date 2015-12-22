from django.conf.urls import url
from .views import TemplateView, CreateTaskView, TaskDetailView,AproveView,DeclineView,TaskListView,TaskEditView,TaskDeleteView

urlpatterns = [
    url(r'^$',TemplateView.as_view()),
    url(r'^create/',CreateTaskView.as_view()),
    url(r'^edit/(?P<id>[0-9]+)',TaskEditView.as_view()),
    url(r'^edit/',TaskEditView.as_view()),
    url(r'^list/',TaskListView.as_view()),
    url(r'^remove/(?P<id>[0-9]+)',TaskDeleteView.as_view()),
    url(r'^aprove/(?P<id>[0-9]+)',AproveView.as_view()),
    url(r'^decline/(?P<id>[0-9]+)',DeclineView.as_view()),
    url(r'^detail/(?P<id>[0-9]+)',TaskDetailView.as_view()),


]
