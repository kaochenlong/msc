from django.db import models


class Interview(models.Model):
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    interview_date = models.DateField(null=True)
    review = models.TextField()
    rating = models.PositiveSmallIntegerField(
        help_text="1 ~ 10 分，1 分最低、10 分最高",
    )
    result = models.CharField(max_length=100, null=True)


class Comment(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
