from django.test import TestCase
from django.contrib.auth.models import User
from .models import Todo
from datetime import datetime, timedelta


class TodoModelTest(TestCase):
    """Test cases for the Todo model"""

    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.todo = Todo.objects.create(
            title='Test Todo',
            description='Test Description',
            user=self.user
        )

    def test_todo_creation(self):
        """Test that a todo can be created"""
        self.assertEqual(self.todo.title, 'Test Todo')
        self.assertEqual(self.todo.user, self.user)
        self.assertFalse(self.todo.is_completed)

    def test_todo_with_due_date(self):
        """Test that a todo can have a due date"""
        due_date = datetime.now() + timedelta(days=1)
        todo = Todo.objects.create(
            title='Todo with due date',
            user=self.user,
            due_date=due_date
        )
        self.assertEqual(todo.due_date, due_date)

    def test_mark_as_completed(self):
        """Test marking a todo as completed"""
        self.todo.is_completed = True
        self.todo.save()
        self.assertTrue(self.todo.is_completed)

    def test_todo_string_representation(self):
        """Test todo string representation"""
        self.assertEqual(str(self.todo), 'Test Todo')
