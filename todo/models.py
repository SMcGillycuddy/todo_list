#import the Django package that allows us to interact with databases 
from django.db import models

#define the database
class List(models.Model):

	#items are text
	item = models.CharField(max_length=200)
	#completed is True / False
	completed = models.BooleanField(default=False)


	def __str__(self):
		return self.item + " | " + str(self.completed)









