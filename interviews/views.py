from django.shortcuts import render, get_object_or_404
from .models import Interview
from django.http import HttpResponse


def index(request):
    if request.POST:
        # 新增
        company_name = request.POST["company_name"]
        position = request.POST["position"]
        interview_date = request.POST["interview_date"]
        review = request.POST["review"]
        result = request.POST["result"]
        rating = request.POST["rating"]

        Interview.objects.create(
            company_name=company_name,
            position=position,
            interview_date=interview_date,
            review=review,
            result=result,
            rating=rating,
        )

        return HttpResponse("新增")
    else:
        interviews = Interview.objects.all()
        return render(
            request,
            "interviews/index.html",
            {"interviews": interviews},
        )


def show(req, id):
    # pk = primary key
    interview = get_object_or_404(Interview, pk=id)

    return render(
        req,
        "interviews/show.html",
        {"interview": interview},
    )


def new(req):
    return render(req, "interviews/new.html")
