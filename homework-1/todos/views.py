from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Todos.
    
    Provides CRUD operations and custom actions:
    - list: Get all todos for the authenticated user
    - create: Create a new todo
    - retrieve: Get a specific todo
    - update: Update a todo
    - partial_update: Partially update a todo
    - destroy: Delete a todo
    - mark_completed: Mark a todo as completed
    - mark_incomplete: Mark a todo as incomplete
    """
    
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return todos for the current authenticated user"""
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Create a new todo for the current user"""
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def mark_completed(self, request, pk=None):
        """Mark a todo as completed"""
        todo = self.get_object()
        todo.is_completed = True
        todo.save()
        serializer = self.get_serializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def mark_incomplete(self, request, pk=None):
        """Mark a todo as incomplete"""
        todo = self.get_object()
        todo.is_completed = False
        todo.save()
        serializer = self.get_serializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def completed(self, request):
        """Get all completed todos for the current user"""
        todos = self.get_queryset().filter(is_completed=True)
        serializer = self.get_serializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def pending(self, request):
        """Get all pending (incomplete) todos for the current user"""
        todos = self.get_queryset().filter(is_completed=False)
        serializer = self.get_serializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
