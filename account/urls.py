from django.urls import path
from account import views

urlpatterns = [
    # path('login',views.our_login),
    path("signup", views.signup_view),
    # path('logout',views.our_logout),
]
