from django.http import HttpResponse
from .models import Course
from django.shortcuts import render
import os

# Create your views here.


def index(request):
    courses = Course.objects.all()
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'templates\\courses.html')
    return render(request, filename, {'courses': courses})
