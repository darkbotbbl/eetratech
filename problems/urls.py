from django.urls import path

from .views import ProblemDetailView


app_name = "problems"

urlpatterns = [
    path('problems/', ProblemDetailView.as_view(), name="problem-detail"),
]
