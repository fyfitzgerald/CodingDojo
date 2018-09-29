from django.shortcuts import render, redirect
from.models import *

from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, "first_app/index.html")


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
            return redirect("/success")
    return redirect("/")


def validate_login(request):
    user_logging_in = User.objects.filter(email=request.POST['email'])
    if len(user_logging_in) == 0:
        messages.error(request, "No matching user")
        return redirect("/")
    elif not bcrypt.checkpw(request.POST['pword'].encode(), user_logging_in[0].password.encode()):
        messages.error(request, "Password is incorrect")
        return redirect("/")
    else:
        print("failed password")
        request.session["username"] = user_logging_in[0].first_name
        request.session["user_id"] = user_logging_in[0].id
        return redirect("/success")
    return redirect("/")


def success(request):
    context = {
        'written_messages': Message.objects.all(),
        'written_comments': Comment.objects.all(),
    }
    return render(request, "first_app/the_wall.html", context)

def post_message(request):
    if request.method == "POST":
        #you label user_id as such bc of [see commented-out line below it]
        Message.objects.create(message=request.POST['message_input'], user_id=request.session['user_id'])
        # Message.objects.create(message=request.POST['message_input'], user=User.objects.get(id=request.session['user_id']))
    return redirect("/success")

def post_comment(request):
    if request.method == "POST":
        #from form/HTML to server/request.session
        Comment.objects.create(comment=request.POST['comment_input'], user=User.objects.get(id=request.session['user_id']), message_c=Message.objects.get(id=request.POST['message_id']))
    return redirect("/success")

def delete_message(request):
    Message.objects.get(id=request.POST['message_id']).delete()
    return redirect("/success")

def delete_comment(request):
    Comment.objects.get(id=request.POST['comment_id']).delete()
    return redirect("/success")