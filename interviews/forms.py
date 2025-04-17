from django.forms import ModelForm, DateInput
from .models import Interview


class InterviewForm(ModelForm):
    class Meta:
        model = Interview
        fields = [
            "company_name",
            "position",
            "result",
            "rating",
            "review",
            "interview_date",
        ]
        labels = {
            "company_name": "公司名稱",
            "position": "職稱",
            "interview_date": "面試日期",
            "result": "面試結果",
            "rating": "評比",
            "review": "心得",
        }
        widgets = {
            "interview_date": DateInput({"type": "date"}),
        }
