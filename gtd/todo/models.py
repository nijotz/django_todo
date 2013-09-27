# I have to be honest, this is all pretty much copied verbatim from
# www.sitepoint.com/build-to-do-list-30-minutes/
# so far it has only taken me 2 weeks to get it to work.

from django.db import models

# Create your models here.

class TodoList(models.Model):
	title = models.CharField(max_length=250, unique=True)
	def __str__(self):
		return self.title

	class Meta:
		ordering = ['title']

	class Admin:
		pass

import datetime

PRIORITY_CHOICES = (
	(1, 'low'),
	(2, 'medium'),
	(3, 'high'),

)

class TodoItem(models.Model):
	title = models.CharField(max_length=250)
	created_date = models.DateTimeField(default=datetime.datetime.now)
	priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
	completed = models.BooleanField(default=False)
	todo_lists = models.ManyToManyField(TodoList, blank=True, null=True)
	def __str__(self):
		return self.title
	class Meta:
		ordering = ['-priority', 'title']
	class Admin:
		pass


