from django.shortcuts import render, get_object_or_404, redirect
from .models import Interview


def index(request):
    if request.POST:
        # 新增
        company_name = request.POST["company_name"]
        position = request.POST["position"]
        interview_date = request.POST["interview_date"]
        review = request.POST["review"]
        result = request.POST["result"]
        rating = request.POST["rating"]

        interview = Interview.objects.create(
            company_name=company_name,
            position=position,
            interview_date=interview_date,
            review=review,
            result=result,
            rating=rating,
        )

        return redirect("interviews:show", interview.id)
    else:
        interviews = Interview.objects.order_by("-id")
        return render(
            request,
            "interviews/index.html",
            {"interviews": interviews},
        )


def show(request, id):
    if request.POST:
        company_name = request.POST["company_name"]
        position = request.POST["position"]
        interview_date = request.POST["interview_date"]
        review = request.POST["review"]
        result = request.POST["result"]
        rating = request.POST["rating"]

        interview = get_object_or_404(Interview, pk=id)

        interview.company_name = company_name
        interview.position = position
        interview.interview_date = interview_date
        interview.review = review
        interview.result = result
        interview.rating = rating

        # 更新
        interview.save()
        return redirect("interviews:show", interview.id)
    else:
        interview = get_object_or_404(Interview, pk=id)

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
