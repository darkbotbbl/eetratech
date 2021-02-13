from django.db import models


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
	created = models.DateTimeField(auto_now_add=True)
	deadline = models.DateTimeField()
	# todo - add an answers field
	# todo - add an admin answer field
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
	file_one = models.FielField(
		upload_to="problems/files",
		null=True,
		blank=True,
	)
	file_two = models.FielField(
		upload_to="problems/files",
		null=True,
		blank=True,
	)
	file_three = models.FielField(
		upload_to="problems/files",
		null=True,
		blank=True,
	)