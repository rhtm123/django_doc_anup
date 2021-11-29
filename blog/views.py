from django.shortcuts import render, HttpResponse

from blog.models import Blog

# Create your views here.


def single_blog(request, pk):
    try:
        b = Blog.objects.get(id=pk)
    except:
        return HttpResponse("Page not found!!")
    return render(request, "single_blog.html", {"blog": b})


def home(request):
    return render(request, "home.html")


def blog_home(req):
    blog_objects = Blog.objects.all()
    context_dict = {"name": "Anup Raj", "blogs": blog_objects}
    return render(req, "blog_home.html", context_dict)


def demo_html(req):
    return render(req, "demo.html")


def contact_view(request):
    return HttpResponse("Contact")


def about_view(request):
    return HttpResponse("about")
