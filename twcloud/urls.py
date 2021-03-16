from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('cloud.routes')),
    path('admin/', admin.site.urls),
]