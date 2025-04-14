from django.shortcuts import render


def index(req):
    return render(req, "interviews/index.html")


def new(req):
    return render(req, "interviews/new.html")
