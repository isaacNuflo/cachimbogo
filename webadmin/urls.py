from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ,name = 'index'),
    path('questionBrowser/',views.questionBrowser, name='browser'),
    path('questionUpdate/<int:id>',views.questionUpdate, name='update'),
];