from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
# Create your views here.
def index(request):
    context = {
        "date": strftime("%m-%d-%Y", localtime()),
        "time": strftime("%I:%M %p", localtime())
    }
    return render(request, 'first_app/index.html', context)