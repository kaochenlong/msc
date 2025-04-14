from django.db import models


class Interview(models.Model):
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    interview_date = models.DateField(null=True)
    review = models.TextField()
    rating = models.PositiveSmallIntegerField()
    result = models.CharField(max_length=100, null=True)
