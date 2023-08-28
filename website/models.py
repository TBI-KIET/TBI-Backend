from django.db import models
from django.utils.text import slugify


class Events(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    eventDate = models.DateField()
    venue = models.TextField()
    image = models.ImageField(null=True, blank=True)
    occured = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = 'Events'
        ordering = ['eventDate']


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)