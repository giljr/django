from django.urls import path
from blog import views
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('about/', views.about, name='about_page'),
]
