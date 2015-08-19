from django.conf.urls import include, url
from .views import ProfileLoginView, ProfileLogoutView


urlpatterns = [
    url(r'^login/', ProfileLoginView.as_view()),
    url(r'^logout/', ProfileLogoutView.as_view()),
]
