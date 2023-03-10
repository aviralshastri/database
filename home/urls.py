"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

#admin server = olqzi9xauy4vhmjp8k6572b1wedn3stgcrf0

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('teacher',views.teacher,name='teacher'),
    path('student',views.student,name='student'),
    path('Admin',views.Admin,name='Admin'),
    path('contact',views.contact,name='contact')
]
