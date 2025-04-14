from django.shortcuts import render
from .models import Interview


def index(req):
    interviews = Interview.objects.all()
    return render(
        req,
        "interviews/index.html",
        {"interviews": interviews},
    )


def show(req, id):
    # pk = primary key
    interview = Interview.objects.get(pk=id)
    return render(
        req,
        "interviews/show.html",
        {"interview": interview},
    )


def new(req):
    return render(req, "interviews/new.html")
