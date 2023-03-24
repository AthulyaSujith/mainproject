from django.urls import path, include

from . import views
app_name = 'collegeapp'
urlpatterns = [
    path('',views.demo,name='demos'),
    path('register',views.register,name='register'),
    path('loginn',views.loginn,name='loginn'),
    path('logout',views.logout,name='logout'),
    path('student/', views.student, name='student'),
    #path('rsform/', views.rsform, name='rsform'),
    path('about/', views.about, name='about'),




]