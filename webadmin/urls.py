from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index ,name = 'index'),
    url(r'^questionBrowser/$',views.questionBrowser, name='browser'),
    url(r'^questionUpdate/(?P<id>[0-9]+)$',views.questionUpdate, name='update'),
];