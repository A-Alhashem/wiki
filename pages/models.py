from django.db import models

# Create your models here.
class WikiPages(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	last_update = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title + ": " + str(self.last_update)

	def get_absolute_url(self):
		from django.urls import reverse
		return reverse('page-detail', args=[str(self.id)])