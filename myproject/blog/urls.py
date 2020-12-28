from django.urls import path

from blog.views import PostListView, PostDetailView, PostCreateView,PostUpdateView,PostDeleteView, UserPostListView, add_comment

from blog import views

urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),
    path('<int:pk>/share/', views.mail_send_view, name='share_by_email'),
   
]


