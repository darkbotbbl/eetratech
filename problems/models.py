from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse


class Problem(models.Model):
    EASY = "E"
    MEDIUM = "M"
    HARD = "H"
    EXTREME = "Em"
    DIFFICULTY_CHOICES = (
        (EASY, "Easy"),
        (MEDIUM, "Medium"),
        (HARD, "Hard"),
        (EXTREME, "Extreme"),
    )
    PROGRAMMING = "P"
    CIRCUIT_DESIGN = "D"
    WEB_DEVELOPMENT = "W"
    SYSTEMS_DESIGN = "S"
    PROBLEM_CATEGORY = (
        (PROGRAMMING, "Programming"),
        (CIRCUIT_DESIGN, "Electrical Circuit Design"),
        (WEB_DEVELOPMENT, "Web Development"),
        (SYSTEMS_DESIGN, "Electrical Systems Design"),
    )

    title = models.CharField(
        max_length=500, 
        null=False, 
        blank=False, 
        help_text="Enter the problem statement"
    )
    slug = AutoSlugField(
        populate_from="title",
        unique=True
    )
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    # todo - the problem description field needs to be a rich text field
    # todo - you need to add a field so admins can add a code snippet, should the problem require it.
    problem_description = models.TextField()
    difficulty = models.CharField(
        choices=DIFFICULTY_CHOICES,
        default=MEDIUM,
        max_length=50
    )
    points_worth = models.PositiveIntegerField(default=5)
    category = models.CharField(
        choices=PROBLEM_CATEGORY,
        default=PROGRAMMING,
        max_length=50
    )

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
            return reverse("problems:problem-detail", kwargs={"slug": self.slug})
    

class File(models.Model):
    problem = models.ForeignKey(
        Problem,
        related_name="files",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255, help_text="Enter a name to identify this file")
    file = models.FileField(
        upload_to="problems/files/"
    )
      
    def __str__(self):
        return self.title


class Image(models.Model):
    problem = models.ForeignKey(
        Problem,
        related_name="images",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255, help_text="Enter a name to identify this image")
    image = models.ImageField(
        upload_to="problems/images"
    )

    def __str__(self):
        return self.title