from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('api/posts/', PostListView.as_view()),
    path('api/posts/<int:id>/', PostDetailView.as_view()),
]
