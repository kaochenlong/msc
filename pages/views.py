from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
import braintree
from django.contrib import messages
from dotenv import load_dotenv
import os

load_dotenv()


def home(req):
    return render(req, "pages/home.html")


def about(req):
    return render(req, "pages/about.html")


def contact(req):
    return render(req, "pages/contact.html")


def payment(req):
    token = braintree_gateway().client_token.generate()
    return render(req, "pages/payment.html", {"token": token})


@require_POST
def checkout(request):
    result = braintree_gateway().transaction.sale(
        {
            "amount": 10,
            "payment_method_nonce": request.POST["nonce"],
        }
    )

    if result.is_success:
        # 把 User 的角色設定成 vip
        messages.success(request, "付款成功")
    else:
        messages.error(request, "付款失敗")

    return redirect("pages:home")


def braintree_gateway():
    return braintree.BraintreeGateway(
        braintree.Configuration(
            environment=braintree.Environment.Sandbox,
            merchant_id=os.getenv("MERCHANT_ID"),
            public_key=os.getenv("PUBLIC_KEY"),
            private_key=os.getenv("PRIVATE_KEY"),
        )
    )
