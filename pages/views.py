from django.shortcuts import render


def home(req):
    return render(req, "pages/home.html", {"title": [1, 2, 3]})


def about(req):
    return render(req, "pages/about.html")


def contact(req):
    return render(req, "pages/contact.html")
