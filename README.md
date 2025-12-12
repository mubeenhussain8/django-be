# Django REST Framework Learning Journey

This repository documents my learning progress with Django and Django REST Framework. I've been exploring different ways to build RESTful APIs and understanding the various patterns and best practices.

## Project Overview

This is a Django project (`django_rest_main`) that demonstrates REST API development using Django REST Framework. The project includes two main applications: `students` and `employees`, each showcasing different approaches to building APIs.

## Project Structure

```
learn-django/
├── api/                    # Main API application
│   ├── views.py           # API views (function-based, class-based, viewsets)
│   ├── serializers.py     # DRF serializers
│   └── urls.py            # API URL routing
├── students/              # Students app
│   ├── models.py         # Student model
│   ├── views.py          # Basic Django views
│   └── urls.py           # Student URLs
├── employees/             # Employees app
│   └── models.py         # Employee model
├── django_rest_main/      # Main project settings
│   ├── settings.py       # Django configuration
│   └── urls.py           # Root URL configuration
└── db.sqlite3            # SQLite database
```

## What I've Learned

### 1. Django Project Setup
- Created a Django project using `django-admin startproject`
- Set up virtual environment for dependency management
- Configured Django settings for REST Framework
- Installed and configured Django REST Framework

### 2. Django Apps
- Created multiple Django apps (`students`, `employees`, `api`)
- Understood the concept of Django apps as modular components
- Registered apps in `INSTALLED_APPS` in settings

### 3. Database Models
Created two models to practice database operations:

**Student Model** (`students/models.py`):
- `student_id`: CharField
- `name`: CharField
- `branch`: CharField

**Employee Model** (`employees/models.py`):
- `emp_id`: CharField
- `emp_name`: CharField
- `designation`: CharField

- Learned to create migrations with `python manage.py makemigrations`
- Applied migrations with `python manage.py migrate`
- Understood model relationships and field types

### 4. Django REST Framework Serializers
- Created `ModelSerializer` classes for both Student and Employee models
- Learned how serializers convert model instances to JSON and vice versa
- Used `fields = "__all__"` to include all model fields

### 5. API Views - Multiple Approaches

I explored different ways to create API endpoints, progressing from simple to more advanced patterns:

#### A. Function-Based Views with `@api_view` Decorator
- Used `@api_view(['GET', 'POST'])` for list/create operations
- Used `@api_view(['GET', 'PUT', 'DELETE'])` for detail operations
- Handled different HTTP methods manually
- Implemented error handling and proper HTTP status codes

**Example**: `studentsView()` and `studentDetailView()` in `api/views.py`

#### B. Class-Based Views with `APIView`
- Created `EmployeeListView` and `EmployeeDetailView` extending `APIView`
- Implemented `get()`, `post()`, `put()`, `patch()`, and `delete()` methods
- Learned about helper methods like `get_object()`
- Better code organization and reusability

#### C. Mixins and GenericAPIView
- Combined `ListModelMixin`, `CreateModelMixin` with `GenericAPIView`
- Used `RetrieveModelMixin`, `UpdateModelMixin`, `DestroyModelMixin`
- Reduced boilerplate code while maintaining flexibility
- Still needed to explicitly call mixin methods

#### D. Generic Views
- Explored `ListAPIView`, `CreateAPIView`, `RetrieveUpdateAPIView`, etc.
- Most concise approach with minimal code
- Automatic method handling

#### E. ViewSets (Current Implementation)
- Implemented `ViewSet` for Employee model
- Created methods: `list()`, `create()`, `retrieve()`, `update()`, `delete()`
- Used with Django REST Framework routers for automatic URL routing
- Clean separation of concerns

### 6. URL Routing
- Set up URL patterns in app-level `urls.py` files
- Included app URLs in main project `urls.py`
- Used URL prefixes (`api/v1/`) for API versioning
- Learned about Django REST Framework routers:
  - `DefaultRouter` for automatic URL generation
  - Registered viewsets with routers
  - Automatic endpoint generation (list, detail, etc.)

### 7. HTTP Status Codes
- `HTTP_200_OK`: Successful GET/PUT requests
- `HTTP_201_CREATED`: Successful POST requests
- `HTTP_204_NO_CONTENT`: Successful DELETE requests
- `HTTP_400_BAD_REQUEST`: Validation errors
- `HTTP_404_NOT_FOUND`: Resource not found

### 8. Error Handling
- Used `try-except` blocks for `DoesNotExist` exceptions
- Used `get_object_or_404()` helper function
- Returned appropriate error responses with proper status codes
- Validated serializer data before saving

## API Endpoints

### Students API (Function-Based Views)
- `GET /api/v1/students/` - List all students
- `POST /api/v1/students/` - Create a new student
- `GET /api/v1/students/<id>/` - Retrieve a specific student
- `PUT /api/v1/students/<id>/` - Update a student
- `DELETE /api/v1/students/<id>/` - Delete a student

### Employees API (ViewSet with Router)
- `GET /api/v1/employees/` - List all employees
- `POST /api/v1/employees/` - Create a new employee
- `GET /api/v1/employees/<id>/` - Retrieve a specific employee
- `PUT /api/v1/employees/<id>/` - Update an employee
- `DELETE /api/v1/employees/<id>/` - Delete an employee

## Technologies Used

- **Django 6.0**: Web framework
- **Django REST Framework 3.16.1**: REST API toolkit
- **SQLite**: Database (default Django database)
- **Python 3.13**: Programming language

## Key Concepts Learned

1. **MVC/MVT Pattern**: Understanding Django's Model-View-Template architecture
2. **RESTful API Design**: Creating RESTful endpoints following best practices
3. **Serialization**: Converting between Python objects and JSON
4. **CRUD Operations**: Create, Read, Update, Delete operations
5. **View Patterns**: Different ways to structure views (function-based, class-based, viewsets)
6. **URL Routing**: Organizing and routing URLs in Django
7. **Database Migrations**: Managing database schema changes
8. **HTTP Methods**: Proper use of GET, POST, PUT, DELETE
9. **Status Codes**: Appropriate HTTP status codes for different scenarios

## Running the Project

1. Activate virtual environment:
   ```bash
   source venv/bin/activate
   ```

2. Run migrations:
   ```bash
   python manage.py migrate
   ```

3. Start development server:
   ```bash
   python manage.py runserver
   ```

4. Access the API:
   - API endpoints: `http://127.0.0.1:8000/api/v1/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Next Steps / Future Learning

- [ ] Authentication and Permissions
- [ ] Pagination
- [ ] Filtering and Searching
- [ ] Testing (Unit tests, Integration tests)
- [ ] API Documentation (Swagger/OpenAPI)
- [ ] Nested Serializers
- [ ] Custom Serializer Fields
- [ ] Model Relationships (ForeignKey, ManyToMany)
- [ ] Custom Permissions
- [ ] Throttling
- [ ] Caching
- [ ] Production deployment considerations

## Notes

- The commented-out code in `api/views.py` shows the progression of learning different view patterns
- Started with function-based views, then moved to class-based views, and finally to viewsets
- This demonstrates understanding of different abstraction levels in Django REST Framework

---

**Learning Date**: 2024  
**Django Version**: 6.0  
**DRF Version**: 3.16.1

