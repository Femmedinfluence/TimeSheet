from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User

#user = User.objects.create_user('mariam', 'mariamkeita@psimali.org', '12345678')
def render_login(request):
    return render(request, "login.html")

def perform_login(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = authenticate(request, username=username, password=password)
        if user_obj is not None:
            login(request, user_obj)
            return HttpResponseRedirect(reverse("admin_dashboard"))
        else:
            messages.error(request, "Le nom d'utilisateur ou le mot de passe n'est pas valide")
            return HttpResponseRedirect("/")
def admin_dashboard(request):
    return render(request, "admin_dashboard.html")

