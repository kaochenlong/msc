from django.shortcuts import render, get_object_or_404, redirect
from .models import Interview, FavoriteInterview
from .forms import InterviewForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def index(request):
    if request.POST:
        form = InterviewForm(request.POST)
        interview = form.save(commit=False)
        interview.user = request.user
        interview.save()
        return redirect("interviews:show", interview.id)
    else:
        interviews = Interview.objects.order_by("-id")
        return render(
            request,
            "interviews/index.html",
            {"interviews": interviews},
        )


@login_required
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


@login_required
def new(req):
    form = InterviewForm()
    return render(req, "interviews/new.html", {"form": form})


@login_required
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


@login_required
def delete(req, id):
    interview = get_object_or_404(Interview, pk=id)
    interview.delete()

    return redirect("interviews:index")


@require_POST
@login_required
def comment(request, id):
    interview = get_object_or_404(Interview, pk=id)
    interview.comment_set.create(
        content=request.POST["content"],
        user=request.user,
    )
    return redirect("interviews:show", interview.id)


@require_POST
@login_required
def favorite(request, id):
    interview = get_object_or_404(Interview, pk=id)
    user = request.user

    if user.favorite_interviews.filter(pk=interview.pk).exists():
        user.favorite_interviews.remove(interview)
    else:
        user.favorite_interviews.add(interview)

    return redirect("interviews:show", interview.id)
