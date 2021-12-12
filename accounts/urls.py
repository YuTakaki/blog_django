from django.contrib.staticfiles.urls import urlpatterns
from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
  path("sign-in", views.signIn, name= "sign-in"),
  path("sign-up", views.signUp, name= "sign-up"),
  path("logout", views.logoutview, name= "logout")
]