from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('userloginform1/', views.userloginform1, name='userloginform1'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-task/', views.add_task, name='add_task'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('test-email/', views.send_test_email, name='test_email'),
    path('tasks/', views.view_tasks, name='view_tasks'),
]


