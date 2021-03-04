from django.contrib import admin

from .models import StudentSolution, RecommendedSolution, File, Image


class ImageInline(admin.StackedInline):
        model = Image
        extra = 1
        max_num = 10


class FileInline(admin.StackedInline):
        model = File
        extra = 1
        max_num = 10

class StudentSolutionAdmin(admin.ModelAdmin):
	list_display = ["title"]
	inlines = [
        ImageInline,
        FileInline,
    ]

class RecommendedSolutionAdmin(admin.ModelAdmin):
	list_display = ["title"]
	inlines = [
        ImageInline,
        FileInline,
    ]

admin.site.register(StudentSolution, StudentSolutionAdmin)
admin.site.register(RecommendedSolution, RecommendedSolutionAdmin)