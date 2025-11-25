# Django TODO Application

This is the first homework from the ai-dev-tools-zoomcamp.

A simple Django REST API application for managing TODO items with support for:
- Create, read, update, and delete TODOs
- Assign due dates to TODOs
- Mark TODOs as resolved/completed
- Filter TODOs by completion status
- User-based TODO management (each user has their own todos)

## Setup Instructions

### 1. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run migrations
```bash
python manage.py migrate
```

### 4. Create a superuser (admin)
```bash
python manage.py createsuperuser
```

### 5. Run the development server
```bash
python manage.py runserver
```

Visit `http://localhost:8000/todos/` to access the web interface.

## Frontend

The application features a modern, responsive web interface built with **Tailwind CSS**:

- **Beautiful UI** - Clean, modern design with gradient backgrounds and smooth animations
- **Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices
- **Task Management** - Intuitive interface for creating, editing, and deleting tasks
- **Filtering & Search** - Filter tasks by status (All/Pending/Completed) and search by title
- **Real-time Updates** - Mark tasks complete/incomplete with instant visual feedback
- **User-friendly Forms** - Simple forms for creating and editing tasks with validation

### Web Routes

- `/todos/` - Main task list page with filtering and search
- `/todos/create/` - Create a new task
- `/todos/<id>/edit/` - Edit an existing task
- `/todos/<id>/delete/` - Delete a task

## API Endpoints

### Authentication
The API uses Django's built-in authentication. You'll need to be logged in to access the API.

### TODO Endpoints

- `GET /api/todos/` - List all todos for the authenticated user
- `POST /api/todos/` - Create a new todo
- `GET /api/todos/{id}/` - Get a specific todo
- `PUT /api/todos/{id}/` - Update a todo
- `PATCH /api/todos/{id}/` - Partially update a todo
- `DELETE /api/todos/{id}/` - Delete a todo

### Custom Actions

- `POST /api/todos/{id}/mark_completed/` - Mark a todo as completed
- `POST /api/todos/{id}/mark_incomplete/` - Mark a todo as incomplete
- `GET /api/todos/completed/` - Get all completed todos
- `GET /api/todos/pending/` - Get all pending todos

## Example TODO Object

```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "due_date": "2024-11-21T18:00:00Z",
  "is_completed": false,
  "created_at": "2024-11-20T10:30:00Z",
  "updated_at": "2024-11-20T10:30:00Z"
}
```

## Admin Interface

You can manage TODOs through the Django admin interface at `/admin/`. Log in with your superuser credentials.

## Running Tests

```bash
python manage.py test
```

## Features

✅ Create TODOs with title and optional description
✅ Assign due dates to TODOs
✅ Mark TODOs as completed/incomplete
✅ Delete TODOs
✅ Filter TODOs by completion status (All/Pending/Completed)
✅ Search TODOs by title
✅ User-based todo management
✅ Admin interface for management
✅ Beautiful web interface with Tailwind CSS
✅ Responsive design (mobile, tablet, desktop)
✅ REST API with Django REST Framework
✅ Unit tests included

## Technology Stack

- **Backend**: Django 4.2.7
- **API**: Django REST Framework 3.14.0
- **Frontend**: Tailwind CSS (via CDN)
- **Database**: SQLite (development)
- **Authentication**: Django built-in authentication
