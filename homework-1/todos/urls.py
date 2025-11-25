from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TodoViewSet, 
    todo_list, 
    todo_create, 
    todo_edit, 
    todo_mark_completed, 
    todo_mark_incomplete, 
    todo_delete
)

router = DefaultRouter()
router.register(r'api/todos', TodoViewSet, basename='api-todo')

urlpatterns = [
    # HTML Views
    path('', todo_list, name='todo_list'),
    path('create/', todo_create, name='todo_create'),
    path('<int:pk>/edit/', todo_edit, name='todo_edit'),
    path('<int:pk>/mark_completed/', todo_mark_completed, name='todo_mark_completed'),
    path('<int:pk>/mark_incomplete/', todo_mark_incomplete, name='todo_mark_incomplete'),
    path('<int:pk>/delete/', todo_delete, name='todo_delete'),
    
    # API Routes
    path('', include(router.urls)),
]
