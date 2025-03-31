from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path(
        'category/<slug:slug>/',
        views.CategoryPostsView.as_view(),
        name='category_posts'
    )
]
