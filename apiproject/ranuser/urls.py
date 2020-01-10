from django.urls import path

from . import views

app_name = 'myapp'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('users', views.UserView,name= 'user'),
    path('list', views.UserListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.UserDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/',views.UserDeleteView.as_view(), name='delete'),
]
