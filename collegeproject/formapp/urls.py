from django.urls import path

from formapp.views import form_view, get_courses

app_name = 'formapp'
urlpatterns = [
    path('form_view/', form_view, name='form_view'),
    path('get_courses/', get_courses, name='get_courses'),

]


