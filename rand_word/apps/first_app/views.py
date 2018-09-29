from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# Create your views here.

def index(request):
    return render(request, "first_app/index.html")


def increment(request):
    unique_id = get_random_string(length=14)
    if 'counter' not in request.session:
        request.session['counter'] = 0
    print (request.session['counter'])
    context = {
        'string': unique_id,
        'counter': request.session['counter']
    }
    request.session['counter'] += 1
    return render(request, 'first_app/index.html', context)


def reset(request):
    request.session.clear()
    return redirect('/')