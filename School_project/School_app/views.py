from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

# Create your views here.
from .models import Department, Course


def demo(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('demo2')
        else:
            messages.info(request, "invalid...ID and Password")
            return redirect('login')
    return render(request, 'login.html')


def demo2(request):
    return render(request, 'demo.html')


def reg_one(request):
    if request.method == 'POST':
        un = request.POST['username']
        np = request.POST['password']
        cp = request.POST['cpassword']
        if np == cp:
            if User.objects.filter(username=un).exists():
                messages.info(request, "!! Username already exists !!")
                return redirect('reg_one')
            else:
                user = User.objects.create_user(username=un, password=np)
                user.save()
                print("User Created")
                return redirect('login')

        else:
            messages.info(request, "!! Password mismatch !!")
            return redirect('reg_one')

    return render(request, 'reg_one.html')


def form(request):
    program = Department.objects.all()
    d = {'program': program}
    return render(request, 'details.html', d)


def load_courses(request):
    programming_id = request.GET.get('programming')
    courses = Course.objects.filter(programming_id=programming_id).order_by('name')
    return render(request, 'branches.html', {'courses': courses})


def pending(request):
    return render(request, 'pending.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

