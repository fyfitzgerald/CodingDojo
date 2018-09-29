from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

# Create your views here.
def index(request):
    return render(request, "first_app/index.html")

def add(request):
    if request.method == 'POST':
        time = strftime('%M %D %Y %#H:%M %S %p', localtime())
        request.session['color'] = request.POST['color']
        request.session['word'] = request.POST['word']
        if 'choices' not in request.session:
            request.session['choices'] = [{
                'words': request.session['word'],
                'colors': request.session['color'],
                'time': strftime,
            }]
            return redirect("/")

        else:
            holder = request.session['choices']
            holder.append({"words": request.POST["word"], "colors": request.POST["color"], "big_font": request.POST["big_font"]})
            request.session['choices'] = holder
            return redirect('/')

    else:
        return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')