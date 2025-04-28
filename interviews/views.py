from django.shortcuts import render, get_object_or_404, redirect
from .models import Interview
from .forms import InterviewForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages


def index(request):
    if request.POST:
        form = InterviewForm(request.POST)
        interview = form.save(commit=False)
        interview.user = request.user
        interview.save()
        messages.success(request, "新增面試成功")
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
        messages.success(request, "面試已更新")
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

    messages.success(req, "面試已刪除")
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
    favorites = request.user.favorite_interviews

    if favorites.filter(pk=interview.pk).exists():
        favorites.remove(interview)
    else:
        favorites.add(interview)

    return render(
        request,
        "interviews/favorite.html",
        {
            "user": request.user,
            "interview": interview,
        },
    )
