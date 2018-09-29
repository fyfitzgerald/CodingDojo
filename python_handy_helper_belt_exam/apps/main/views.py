from django.shortcuts import render, redirect
import bcrypt
# Create your views here.
from django.contrib import messages
from datetime import datetime
from ..loginreg.models import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


# Create your views here.

def main(request):
    if 'user_id' not in request.session:
        messages.error(request, "Invalid login")
        return redirect("/")
    context = {
        'user': User.objects.get(id=request.session['user_id']).job_created.all(),
        'user_name' : User.objects.get(id=request.session['user_id']),
        'all_jobs': Job.objects.all(),
    }
    return render(request, "main/home.html", context)

def add_a_job(request):
    # user = User.objects.get(id=request.session['user_id'])
    # if not user == request.session['user_id']:
    # if request.method == "GET":
    #     return redirect ('/')
    return render(request, "main/addajob.html")

def process_job_add(request):
    if request.method == "POST":
        errors = Job.objects.basic_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/main/addajob")
        else:
            print(request.POST)
            Job.objects.create(title=request.POST['title'], description=request.POST['description'], location=request.POST['location'], user_created=User.objects.get(id=request.session['user_id']))
            return redirect('/main/main')

def view_job(request, number):
    job = Job.objects.get(id=number)
    context = {
        'this_job': job,
        'user1': User.objects.get(id=request.session['user_id']).job_created.all(),
        'created_job': Job.objects.filter(id=request.session['user_id'])
    }
    print (context)
    return render(request, "main/viewjob.html", context)

def edit_job(request, number):
    # user = User.objects.get(id=request.session['user_id'])
    # if not user == request.session['user_id']:
    #     return redirect ('/')
    job = Job.objects.get(id=number)
    context = {
        'this_job': job,
    }
    return render(request, "main/editjob.html", context)

def process_job_update(request, id):
    if request.method == "POST":
        errors = Job.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                job = Job.objects.get(id=id)
            return redirect('/main/edit_job/'+str(id))
        else:
            print(request.POST)
            job = Job.objects.get(id=request.POST['job_id'])
            job.title = request.POST['title']
            job.description = request.POST['description']
            job.location = request.POST['location']
            job.save()
            return redirect('/main/main')

def delete_job(request, number):
    job = Job.objects.get(id=number)
    job.delete()
    return redirect('/main/main')

def logout(request):
    request.session.clear()
    return render(request, "loginreg/index.html")
