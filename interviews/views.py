from django.shortcuts import render, get_object_or_404, redirect
from .models import Interview, Comment
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
        comments = interview.comment_set.all()
        return render(
            request,
            "interviews/show.html",
            {"interview": interview, "comments": comments},
        )


def new(req):
    form = InterviewForm()
    return render(req, "interviews/new.html", {"form": form})


def edit(req, id):
    interview = get_object_or_404(Interview, pk=id)
    form = InterviewForm(instance=interview)
    return render(
        req,
        "interviews/edit.html",
        {
            "interview": interview,
            "form": form,
        },
    )


def delete(req, id):
    interview = get_object_or_404(Interview, pk=id)
    interview.delete()

    return redirect("interviews:index")


def comment(request, id):
    interview = get_object_or_404(Interview, pk=id)
    interview.comment_set.create(content=request.POST["content"])
    return redirect("interviews:show", interview.id)
