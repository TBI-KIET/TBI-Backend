from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class Events(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    eventDate = models.DateField()
    venue = models.TextField()
    image = models.ImageField(null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Events'
        ordering = ['eventDate']

    def __str__(self):
        return self.title
    
    def is_past(self):
        return self.eventDate < timezone.now()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class ContactUs(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    subject = models.TextField()
    message = models.TextField()


    def __str__(self):
        return f'{self.name} {self.subject}'
