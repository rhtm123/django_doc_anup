from django.shortcuts import render, HttpResponse

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

# Create your views here.


def logout_view(request):
    logout(request)
    return HttpResponse("You are successfully logged out")


def login_view(request):
    d = {
        "is_login": False,
    }
    if request.method == "POST":
        username1 = request.POST["username"]
        password1 = request.POST["pass"]
        u = authenticate(username=username1, password=password1)
        if u:
            login(request, u)
            d = {"is_login": True}

            return render(request, "account/login.html", d)
        else:
            return HttpResponse("Your credentials are not correct")
    return render(request, "account/login.html")


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
