from django.shortcuts import render
from .forms import mform
from .models import Department, Course
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

def form_view(request):
    if request.method == 'POST':
        form = mform(request.POST)
        if form.is_valid():
            return render(request, 'confirm.html')
            pass
    else:
        form = mform()
    return render(request, 'my_form.html', {'form': form})


from django.http import JsonResponse

def get_courses(request):
    department_value = request.GET.get('department')
    if department_value == 'CSE':
        courses = {'IT1': 'Computer Security', 'IT2': 'Cloud computing', 'IT3': 'System Administration',
                      'IT4': 'Cryptograpy','IT5': 'Cyber Securiry'}
    elif department_value == 'Li':
        courses = { 'LI1': 'Modern Literature',  'LI2': 'Grammar',  'LI3': 'Journalism',  'LI4': 'medieval',  'LI5': 'Folklore'}
    elif department_value == 'ARTS':
        courses = { 'Arts1': 'English',  'Arts2': 'Malayalam',  'Arts3': 'Hindi',  'Arts4': 'Homescience',  'Arts5': 'Finearts'}
    elif department_value == 'SE':
        courses = {  'SE1': 'History',  'SE2': 'Geography',  'SE3': 'Anthropology',  'SE4': 'Political Science',  'SE5': 'Psycology'}
    elif department_value == 'CC':
        courses = { 'CC1': 'Banking', 'CC2': 'BA', 'CC3': 'BBA', 'CC4': 'CA', 'CC5': 'BCOM'}
    elif department_value == 'S':
        courses = { 'S1': 'Physics', 'S2': 'Chemistry', 'S3': 'Zoology', 'S4': 'Botony', 'S5': 'MicroBiology'}
    elif department_value == 'N':
        courses = {'N1': '---'}

    else:
        courses = {}
    return JsonResponse(courses)