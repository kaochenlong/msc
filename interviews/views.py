from django.shortcuts import render, get_object_or_404, redirect
from .models import Interview
from .forms import InterviewForm


def index(request):
    if request.POST:
        form = InterviewForm(request.POST)
        interview = form.save()
        return redirect("interviews:show", interview.id)
    else:
        interviews = Interview.objects.order_by("-id")
        return render(
            request,
            "interviews/index.html",
            {"interviews": interviews},
        )


def show(request, id):
    interview = get_object_or_404(Interview, pk=id)

    if request.POST:
        form = InterviewForm(request.POST, instance=interview)
        form.save()
        return redirect("interviews:show", interview.id)
    else:
        return render(
            request,
            "interviews/show.html",
            {"interview": interview},
        )


def new(req):
    return render(req, "interviews/new.html")


def edit(req, id):
    interview = get_object_or_404(Interview, pk=id)
    return render(req, "interviews/edit.html", {"interview": interview})


def delete(req, id):
    interview = get_object_or_404(Interview, pk=id)
    interview.delete()

    return redirect("interviews:index")
