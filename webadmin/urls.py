from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('questionBrowser/', views.questionBrowser, name='browser'),
    path('questionUpdate/<int:id>', views.questionUpdate, name='update'),
    path('questionCreate/', views.questionCreate, name='create'),
];