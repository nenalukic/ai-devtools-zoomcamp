from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Todo
from .serializers import TodoSerializer


# ============= HTML Views (Frontend) =============

@login_required(login_url='/admin/login/')
def todo_list(request):
    """Display list of all todos for the current user"""
    todos = Todo.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'todos/todo_list.html', {'todos': todos})


@login_required(login_url='/admin/login/')
def todo_create(request):
    """Create a new todo"""
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date') or None
        
        todo = Todo.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            user=request.user
        )
        return redirect('todo_list')
    
    return render(request, 'todos/todo_form.html')


@login_required(login_url='/admin/login/')
def todo_edit(request, pk):
    """Edit an existing todo"""
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.due_date = request.POST.get('due_date') or None
        todo.is_completed = 'is_completed' in request.POST
        todo.save()
        return redirect('todo_list')
    
    return render(request, 'todos/todo_form.html', {'form': type('Form', (), {'instance': todo})()})


@login_required(login_url='/admin/login/')
@require_http_methods(["POST"])
def todo_mark_completed(request, pk):
    """Mark a todo as completed"""
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.is_completed = True
    todo.save()
    return JsonResponse({
        'id': todo.id,
        'title': todo.title,
        'is_completed': todo.is_completed
    })


@login_required(login_url='/admin/login/')
@require_http_methods(["POST"])
def todo_mark_incomplete(request, pk):
    """Mark a todo as incomplete"""
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.is_completed = False
    todo.save()
    return JsonResponse({
        'id': todo.id,
        'title': todo.title,
        'is_completed': todo.is_completed
    })


@login_required(login_url='/admin/login/')
@require_http_methods(["POST"])
def todo_delete(request, pk):
    """Delete a todo"""
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    return JsonResponse({'status': 'success'})


# ============= REST API Views =============

class TodoViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Todos via REST API.
    
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
