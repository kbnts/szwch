from django.urls import path

from . import views

app_name = "shortener"
urlpatterns = [
    path("shrt/", views.UrlShortenerCreateAPIView.as_view()),
]
