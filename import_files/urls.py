from django.conf.urls import url
from .views import ImportView

urlpatterns = [
    url(r'^',ImportView.as_view()),
]
