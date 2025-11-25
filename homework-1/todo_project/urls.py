"""
URL configuration for todo_project project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/todos/', permanent=False)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('todos/', include('todos.urls')),
    path('api/', include('todos.urls')),
]
