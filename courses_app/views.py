from django.shortcuts import render, redirect
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
    

def add_course(request):
    t = request.GET.get('title')
    d = request.GET.get('description')

    if t and d:
        Course.objects.create(title=t, description=d)
        return redirect('/course/list')

    


    return render(request, 'courses_app/add_course.html')