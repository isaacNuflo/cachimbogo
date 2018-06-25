from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('questionBrowser/', views.question_browser, name='browser'),
    path('questionUpdate/<int:id>', views.question_update, name='update'),
    path('questionCreate/', views.question_create, name='create'),
    path('register/', views.register, name='register'),
];