from django.contrib import admin
from .models import Problem, Image, File
from solutions.models import StudentSolution


class ImageInline(admin.StackedInline):
        model = Image
        extra = 1


class FileInline(admin.StackedInline):
        model = File
        extra = 1

class ProblemAdmin(admin.ModelAdmin):
    list_display = ["title", "created"]
    inlines = [
        ImageInline,
        FileInline,
    ]


admin.site.register(Problem, ProblemAdmin)