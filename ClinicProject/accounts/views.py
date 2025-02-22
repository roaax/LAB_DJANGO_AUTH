from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

#-----------REGISTER-----------------
def register_user(request : HttpRequest):

    if request.method == "POST":
        new_user = User.objects.create_user(username=request.POST["username"], email= request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
        new_user.save()
    return render(request, "accounts/register.html")

#-----------LOGIN-----------------
def login_user(request : HttpRequest):
    msg = ""
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])     
        if user:
            login(request, user)
            return redirect("ClinicApp:list_doctors")
        else:
            msg = "Invalid UserName or Password"
    return render(request, "accounts/login.html", {"msg" : msg})

#-----------LOGOUT-----------------
def logout_user(request: HttpRequest):
    logout(request)
    return redirect("ClinicApp:list_doctors")
