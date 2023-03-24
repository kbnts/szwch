from django.urls import path

from apps.entrypoint import views

app_name = "entrypoint"
urlpatterns = [
    path("<str:url_id>/", views.EntrypointView.as_view(), name="entrypoint"),
]
