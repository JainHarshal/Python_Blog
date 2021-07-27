from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
   path("login/",LoginView.as_view(),name="Login"),
   path("logout/",LogoutView.as_view(next_page="Home"),name="Logout"),
]