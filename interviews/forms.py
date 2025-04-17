from django.forms import ModelForm
from .models import Interview


class InterviewForm(ModelForm):
    class Meta:
        model = Interview
        fields = [
            "company_name",
            "position",
            "interview_date",
            "result",
            "rating",
            "review",
        ]
