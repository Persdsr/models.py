from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('comment/<int:pk>/', views.CreateComment.as_view(), name='create_comment'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.Logout, name='logout'),
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_single'),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    #path('', cache_page(60*15)(views.HomeView.as_view()), name='home'),
    path('', views.HomeView.as_view(), name='home'),

]
