from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	avatar = models.ImageField(upload_to="media/users/avatar", null=True, blank=True)
	points = models.PositiveIntegerField(default=0)
	total_upvotes = models.PositiveIntegerField(default=0)
	total_downvotes = models.PositiveIntegerField(default=0)