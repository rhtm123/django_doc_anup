from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

from django.contrib.auth.models import User

# Create your views here.


def signup_view(request):
    # print("Request submitted")
    d = {"is_signup": False}
    if request.method == "POST":
        username1 = request.POST["username"]
        password1 = request.POST["pass"]
        firstname1 = request.POST["fn"]
        lastname1 = request.POST["ln"]
        u = User.objects.create_user(
            username=username1,
            password=password1,
            first_name=firstname1,
            last_name=lastname1,
        )
        u.save()
        d = {"is_signup": True}
        return render(request, "account/signup.html", d)
    return render(request, "account/signup.html", d)
