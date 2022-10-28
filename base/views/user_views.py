from django.shortcuts import render, redirect
from ..forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required


def register(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:

        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = User.objects.create_user(first_name=first_name,

                                                last_name=last_name, email=email, password=password, username=email)
                user.save()

                return redirect("login")

        else:
            form = RegisterForm()
        return render(request, 'register.html', {'form': form})


def login(request):

    if request.user.is_authenticated:
        return redirect("index")
    else:

        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]

            user = auth.authenticate(username=email, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("index")

            else:
                messages.error(request, "Invalid Credentials")
                return redirect("login")

        return render(request, "login.html")


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'you are logged out!')
    return redirect("login")
