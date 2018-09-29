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
        'user': User.objects.get(id=request.session['user_id']),
    #     'user_name' : User.objects.get(id=request.session['user_id']),
        'all_quotes': Quote.objects.all(),
    }
    return render(request, "main/home.html", context)
# Create your views here.

def process_quote_add(request):
    if request.method == "POST":
        errors = Quote.objects.basic_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/main/main")
        else:
            print(request.POST)
            Quote.objects.create(content=request.POST['quote'], author=request.POST['author'], user_created=User.objects.get(id=request.session['user_id']))
            return redirect('/main/main')

def view_user_quotes(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    # user_quoting = User.objects.get(id=request.POST['this_id'])
    # if request.method == "POST":
    user = User.objects.get(id=id)
    quote = Quote.objects.filter(user_created=id)
    context = {
        'this_user': user,
        # 'these_quotes': User.objects.filter(quote_created=id),
        'created_quotes': quote
    }
    return render(request, "main/view_quotes.html", context)

def edit_user_account(request, id):
    # user = User.objects.get(id=request.session['user_id'])
    # if not user == request.session['user_id']:
    #     return redirect ('/')
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=id)
    context = {
        'this_user': user,
    }
    return render(request, "main/edit_acct.html", context)

def process_acct_update(request, id):
    if request.method == "POST":
        errors = messages.error
    first_name_length = request.POST['f_name']
    if len(first_name_length) < 1:
        messages.error(request, "First name must not be left blank")
        return redirect('/main/edit_user_account/'+str(id))
    if len(request.POST['l_name']) < 1:
        messages.error(request, "Last name must not be left blank")
        return redirect('/main/edit_user_account/'+str(id))
    if len(request.POST['email_address']) < 1:
        messages.error(request, "Email must not be left blank")
        return redirect('/main/edit_user_account/'+str(id))
    # if len(errors) > 0:
    #     for key, value in errors.items():
    #         messages.error(request, value)
    #     return redirect('/main/edit_user_account/'+str(id))
    else:
        print(request.POST)
        user = User.objects.get(id=request.POST['user_id'])
        user.first_name = request.POST['f_name']
        user.last_name = request.POST['l_name']
        user.email = request.POST['email_address']
        user.save()
        return redirect('/main/main')

def delete_quote(request, id):
    quote = Quote.objects.get(id=id)
    quote.delete()
    return redirect('/main/main')

def logout(request):
    request.session.clear()
    return render(request, "loginreg/index.html")
