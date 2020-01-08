from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import LoginView, LogoutView




urlpatterns = [
    path('', views.todo_list,name='todo_list'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('login/',LoginView.as_view(), name='login_url'),
    path('logout/',LogoutView.as_view(), name='logout_url'),
    path('register/', views.register, name='register'),
    path('accounts/profile/', views.after_login, name='after_login()')
]