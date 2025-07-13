from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('jobs/', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('apply/<int:job_id>/', views.apply, name='apply'),
    path('success/', views.success, name='success'), 
    # path('', views.job_list, name='job_list'),
    path('chatbot/', views.chatbot, name='chatbot'),
    
]
