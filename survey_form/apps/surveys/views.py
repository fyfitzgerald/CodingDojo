from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "surveys/index.html")

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comments'] = request.POST['comments']
    return redirect('/results')

def results(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    print (request.session['counter'])
    context = {
        'counter': request.session['counter']
    }
    request.session['counter'] += 1
    return render(request, "surveys/results.html", context)