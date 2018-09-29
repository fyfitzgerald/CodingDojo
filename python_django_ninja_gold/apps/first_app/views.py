from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, "first_app/index.html")

def process_money(request):
    time = datetime.now()
    actual_time = time.strftime("%Y-%m-%d %H:%M:%S")
    if request.method == 'POST':
        if request.POST['building'] == "farm":
            number = random.randint(10,20)
            request.session['gold'] += number
            request.session['activities'].append(f"<p class='earn'>Earned {number} gold coins from the farm ({actual_time})</p>")
        if request.POST['building'] == "cave":
            number = random.randint(5,10)
            request.session['gold'] += number
            request.session['activities'].append(f"<p class='earn'>Earned {number} gold coins from the cave ({actual_time})</p>")
        if request.POST['building'] == "house":
            number = random.randint(2,5)
            request.session['gold'] += number
            request.session['activities'].append(f"<p class='earn'>Earned {number} gold coins from the house ({actual_time})</p>")
        if request.POST['building'] == "casino":
            number = random.randint(-50,50)
            request.session['gold'] += number
            if number < 0:
                request.session['activities'].append(f"<p class='lose'>Entered a casino and lost {number} gold coins...Ouch ({actual_time})</p>")
            if number > 0:
                request.session['activities'].append(f"<p class='earn'>Earned {number} gold coins from the casino ({actual_time})</p>")           
    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")