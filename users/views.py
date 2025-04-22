from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST


@require_POST
def index(req):
    form = UserCreationForm(req.POST)
    form.save()

    return redirect("pages:home")


def sign_in(req):
    return render(req, "users/sign_in.html")


@require_POST
def create_session(req):
    username = req.POST["username"]
    password = req.POST["password"]

    user = authenticate(
        username=username,
        password=password,
    )

    if user is not None:
        login(req, user)
        return redirect("pages:home")
    else:
        return redirect("users:sign_in")


def sign_up(req):
    form = UserCreationForm()
    return render(
        req,
        "users/sign_up.html",
        {
            "form": form,
        },
    )
