from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt


from .models import User


def index(request):
    return render(request, "index.html")

def home(request):
    if "user_id" not in request.session:
        return redirect("/")
    user= User.objects.get(id=request.session['user_id'])
    context ={
        "user":user
    }
    return render (request, "home.html", context)

def register(request):

    errors= User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for e in errors.values():
            messages.error(request, e)
        return redirect("/")

    
    pw_hash= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    user=User.objects.create(
    first_name= request.POST["first_name"],
    last_name= request.POST["last_name"],
    email= request.POST["email"], 
    password=pw_hash
    )
   
    request.session["user_id"]= user.id 
    return redirect("/")

def login(request):
    try:
        user= User.objects.get(email= request.POST['email'])
    except:
        messages.error(request, "Invalid email and password!")
        return redirect("/")

    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        request.session["user_id"]= user.id
        return redirect("/tally")

    messages.error(request, "Invalid email and password!")
    return redirect("/")


def logout(request):
    request.session.clear()
    return redirect("/")