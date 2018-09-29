from django.shortcuts import render, HttpResponse, redirect
from.models import *


# Create your views here.
def index(request):
    context = {
        'all_users': User.objects.all()
    }
    return render(request, "first_app/index.html", context)

def new(request):
    return render(request, "first_app/new.html")

def create(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    return redirect("/users")

def show(request, id):
    context = {
        'id': id,
        'first_name': User.objects.get(id=id).first_name,
        'last_name': User.objects.get(id=id).last_name,
        'email': User.objects.get(id=id).email,
        'created_at': User.objects.get(id=id).created_at,
    }
    return render(request, "first_app/show.html", context)

def edit(request, id):
    context = {
        'id': id,
        'first_name': User.objects.get(id=id).first_name,
        'last_name': User.objects.get(id=id).last_name,
        'email': User.objects.get(id=id).email,
        'created_at': User.objects.get(id=id).created_at,
    }
    return render(request, "first_app/edit.html", context)

def update(request, id):
    user = User.objects.get(id=id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    return redirect('/users/'+str(id))

def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect("/users")