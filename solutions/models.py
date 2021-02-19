from django.db import models
from django.contrib.auth import get_user_model
from problems.models import Problem
from autoslug import AutoSlugField

User = get_user_model()


class Solution(models.Model):
	"""
		This is the base solution model
	"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(
		max_length=300, 
		help_text="Enter a short description of the solution",
		blank=False,
		null=False,
	)
	slug = AutoSlugField(
		populate_from="title",
		unique=True
	)
	description_of_answer = models.TextField(
		help_text="Add a text explanation of the problem if there is any",
		null=True,
		blank=True,
	)
	image_one = models.ImageField(
		upload_to="problems/images",
		null=True,
		blank=True
	)
	image_two = models.ImageField(
		upload_to="problems/images",
		null=True,
		blank=True
	)
	image_three = models.ImageField(
		upload_to="problems/images",
		null=True,
		blank=True
	)
	file_one = models.FileField(
		upload_to="solutions/files",
		null=True,
		blank=True,
	)
	file_two = models.FileField(
		upload_to="solutions/files",
		null=True,
		blank=True,
	)
	file_three = models.FileField(
		upload_to="solutions/files",
		null=True,
		blank=True,
	)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-created"]


class StudentSolution(Solution):
	"""
		This is the model for a studen't solution
	"""
	problem = models.ForeignKey(
		Problem,
		related_name="student_solutions",
		on_delete=models.CASCADE,
	)
	upvotes = models.PositiveIntegerField(default=0)
	downvotes = models.PositiveIntegerField(default=0)



class RecommendedSolution(Solution):
	problem = models.ForeignKey(
		Problem,
		related_name="recommended_solution",
		on_delete=models.CASCADE,
	)
	link_to_video = models.URLField(
		max_length=200,
		help_text="Enter link to video posted on youtube, or any video hosting platform",
	)
	