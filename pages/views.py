from django.shortcuts import render
from django.views.generic import ListView

from problems.models import Problem

class HomePageView(ListView):
	model = Problem
	context_object_name = "problems"
	template_name = "pages/homepage.html"