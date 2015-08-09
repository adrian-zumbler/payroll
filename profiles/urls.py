from django.conf.urls import include, url
from .views import ProfileLoginView


urlpatterns = [
    url(r'^login/', ProfileLoginView.as_view()),
]