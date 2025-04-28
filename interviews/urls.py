from django.urls import path
from . import views

app_name = "interviews"

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="new"),
    path("<int:id>", views.show, name="show"),
    path("<int:id>/edit", views.edit, name="edit"),
    path("<int:id>/delete", views.delete, name="delete"),
    path("<int:id>/comment", views.comment, name="comment"),
    path("<int:id>/favorite", views.favorite, name="favorite"),
]
