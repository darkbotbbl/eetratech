from django.urls import path

from .views import RecommendedSolutionDetailView, StudentSolutionDetailView


app_name = "solutions"

urlpatterns = [
    path("student-solution/<str:slug>/", StudentSolutionDetailView.as_view(), name="student-solution"),
    path("recommended-solution/<str:slug>/", RecommendedSolutionDetailView.as_view(), name="recommended-solution"),
]
