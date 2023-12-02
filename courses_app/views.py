from django.shortcuts import render
from .models import Course

def courses_list(request):
    courses = Course.objects.all()

    return render(request,"courses_app/courses_list.html", context={'courses_list':courses})


def course_detail(request, id):
    course = Course.objects.get(id = id )
    course.views += 1
    if course.situation == True:
        course.situation = False
    else:
        course.situation = True
        
    course.save()
    return render(request, "courses_app/course_detail.html", context={'course' : course })
    