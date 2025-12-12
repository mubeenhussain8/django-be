import django_filters
from blogs.models import Blog, Comment
from students.models import Student
from employees.models import Employees

class BlogFilter(django_filters.FilterSet):
    # Custom filtering - exact match
    title = django_filters.CharFilter(field_name='blog_title', lookup_expr='icontains')
    # Filter by title containing text (case-insensitive)
    
    # Custom filtering - date range (if you add created_at later)
    # created_after = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    # created_before = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')
    
    class Meta:
        model = Blog
        fields = ['blog_title']  # Fields you can filter on

class CommentFilter(django_filters.FilterSet):
    blog = django_filters.NumberFilter(field_name='blog__id')
    # Filter comments by blog ID
    
    class Meta:
        model = Comment
        fields = ['blog']

class StudentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    branch = django_filters.CharFilter(field_name='branch', lookup_expr='iexact')
    student_id = django_filters.CharFilter(field_name='student_id', lookup_expr='icontains')
    
    class Meta:
        model = Student
        fields = ['name', 'branch', 'student_id']

class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
    emp_id = django_filters.CharFilter(field_name='emp_id', lookup_expr='icontains')
    
    class Meta:
        model = Employees
        fields = ['emp_name', 'designation', 'emp_id']
