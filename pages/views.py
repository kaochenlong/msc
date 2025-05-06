from django.contrib import messages
from django.shortcuts import render


def home(req):
    messages.success(req, "aaa")
    return render(req, "pages/home.html")


def about(req):
    return render(req, "pages/about.html")


def contact(req):
    return render(req, "pages/contact.html")
