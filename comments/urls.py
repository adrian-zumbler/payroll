from django.conf.urls import include, url
from .views import CommentCreateView, CommentList, CommentView, UpdateCommentView

urlpatterns = [
    url(r'^(?P<id>[0-9])/', UpdateCommentView.as_view()),
    url(r'^create/',CommentCreateView.as_view()),
    url(r'^list/',CommentList.as_view()),
    url(r'^',CommentView.as_view()),

]
