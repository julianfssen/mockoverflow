from django.urls import path, include
from . import views
from .views import (
	PostListView,
	FilteredPostListView,
	PostDetailView,
	PostCreateView,
	PostSolvedView,
	PostUpdateView,
	PostDeleteView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', PostListView.as_view(), name = 'forum-home'),
	path('', FilteredPostListView.as_view(), name='filtered-home'),
	path('post/new/', PostCreateView.as_view(), name = 'post-create'),
	path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
	path('post/<int:pk>/solved/', PostSolvedView.as_view(), name = 'post-solved'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
	path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)