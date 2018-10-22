from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/',include('servicios.urls')),
    path('webadmin/',include('webadmin.urls')),
]
