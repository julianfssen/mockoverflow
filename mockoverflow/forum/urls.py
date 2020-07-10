from django.urls import path, include
from . import views
from .views import (
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
)

urlpatterns = [
	path('', views.home, name = 'forum-home'),
	path('post/new/', PostCreateView.as_view(), name = 'post-create'),
	path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
	path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]