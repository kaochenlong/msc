from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST
from django.urls import reverse


@require_POST
def index(req):
    form = UserCreationForm(req.POST)
    form.save()

    return redirect("pages:home")


def sign_in(req):
    next = req.GET.get("next", reverse("pages:home"))
    return render(req, "users/sign_in.html", {"next": next})


@require_POST
def create_session(req):
    username = req.POST.get("username")
    password = req.POST.get("password")

    user = authenticate(
        username=username,
        password=password,
    )

    if user is not None:
        login(req, user)

        next = req.POST.get("next", "pages:home")
        return redirect(next)
    else:
        return redirect("users:sign_in")


@require_POST
def delete_session(req):
    logout(req)
    return redirect("pages:home")


def sign_up(req):
    form = UserCreationForm()
    return render(
        req,
        "users/sign_up.html",
        {
            "form": form,
        },
    )
