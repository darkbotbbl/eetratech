from django.shortcuts import render
from django.views.generic import DetailView

from .models import Problem


class ProblemDetailView(DetailView):
    model = Problem
    template_name = "problems/problem-detail.html"