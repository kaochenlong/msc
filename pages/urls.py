from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("payment", views.payment, name="payment"),
    path("checkout", views.checkout, name="checkout"),
]
