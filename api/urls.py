from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employee' )
urlpatterns = [
    # Student endpoints (function-based)
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),
    
    # Employee endpoints (class-based using APIView)
    # path('employees/', views.EmployeeListView.as_view(), name='employee-list'),
    # path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    
    path('', include(router.urls)),
    # Blog endpoints
    path('blogs/', views.BlogsView.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    # Comment endpoints
    path('comments/', views.CommentsView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]