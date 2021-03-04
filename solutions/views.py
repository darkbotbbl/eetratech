from django.shortcuts import render
from django.views.generic import DetailView
from .models import RecommendedSolution, StudentSolution

class RecommendedSolutionDetailView(DetailView):
    model = RecommendedSolution
    context_object_name = "recommended_solution"
    template_name = "solutions/recommended_solution_detail.html"


class StudentSolutionDetailView(DetailView):
    model = StudentSolution
    context_object_name = "student_solution"
    template_name = "solutions/student_solution_detail.html"