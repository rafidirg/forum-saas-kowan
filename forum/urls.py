from django.urls import path
from forum import views

app_name = "forum"

urlpatterns = [
  path('', views.home, name='home'),
  path('create/', views.create, name='create_post'),
  path('<slug>/', views.detail, name='detail'),
]