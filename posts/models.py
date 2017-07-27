from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=50)
	image = models.ImageField(upload_to="blog_images", null=True, blank=True)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"post_id": self.id})

	class Meta:
		ordering = ['-timestamp', '-updated']