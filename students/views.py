from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    students = [
        {'id':1, 'name':'mubeen hussain'}
    ]
    # return HttpResponse('<h2>Hello World</h2>')
    return HttpResponse(students)