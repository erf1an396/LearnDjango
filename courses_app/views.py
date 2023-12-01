from django.shortcuts import render
from .models import Course

def courses_list(request):
    courses = Course.objects.all()

    return render(request,"courses_app/courses_list.html", context={'courses_list':courses})


def course_detail(request):
    pass