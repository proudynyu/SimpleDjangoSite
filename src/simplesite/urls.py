from django.urls import path
from . import views

app_name = "simplesite"

urlpatterns = [
    path("", views.homepage, name="homepage")
]