from django.shortcuts import render, redirect
from .models import User
import bcrypt
# Create your views here.
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "loginreg/index.html")


def register(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            print(request.POST)
            hashed_pw = bcrypt.hashpw(request.POST['pword'].encode(), bcrypt.gensalt())
            just_registered = User.objects.create(first_name=request.POST["f_name"], last_name=request.POST["l_name"], email=request.POST["email_address"], password=hashed_pw.decode())
            request.session["username"] = just_registered.first_name
            request.session["user_id"] = just_registered.id
            return redirect("/main/main")
    # return redirect("/loginreg/")


def validate_login(request):
    user_logging_in = User.objects.filter(email=request.POST['email'])
    if len(user_logging_in) == 0:
        messages.error(request, "No matching user")
        return redirect("/")
    elif not bcrypt.checkpw(request.POST['pword'].encode(), user_logging_in[0].password.encode()):
        messages.error(request, "Password is incorrect")
        return redirect("/")
    else:
        # print("failed password")
        request.session["username"] = user_logging_in[0].first_name
        request.session["user_id"] = user_logging_in[0].id
        return redirect("/main/main")


# def success(request):
#     return render(request, "first_app/success.html")   
