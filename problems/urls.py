from django.urls import path

from .views import ProblemDetailView


app_name = "problems"

urlpatterns = [
    path('<str:slug>/', ProblemDetailView.as_view(), name="problem-detail"),
]
