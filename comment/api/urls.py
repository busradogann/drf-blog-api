from django.urls import path

from comment.api.views import (
    CommentCreateAPIView,
    CommentListAPIView,
    CommentUpdateAPIView,
)

app_name = "comment"

urlpatterns = [
    path('create-comment', CommentCreateAPIView.as_view(), name='create'),
    path('list-comment', CommentListAPIView.as_view(), name='list'),
    path('update-comment/<pk>', CommentUpdateAPIView.as_view(), name='update'),
]
