from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def student(request):
    return render(request,'student.html')

def teacher(request):
    return render(request,'teacher.html')

def Admin(request):
    return render(request,'admin.html')

def contact(request):
    return render(request,'contact.html')

    