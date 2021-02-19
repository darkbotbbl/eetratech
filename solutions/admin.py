from django.contrib import admin

from .models import StudentSolution, RecommendedSolution


class StudentSolutionAdmin(admin.ModelAdmin):
	list_display = ["title"]


class RecommendedSolutionAdmin(admin.ModelAdmin):
	list_display = ["title"]


admin.site.register(StudentSolution, StudentSolutionAdmin)
admin.site.register(RecommendedSolution, RecommendedSolutionAdmin)