from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class OurStory(models.Model):
    """
    Stores a single our story entry.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    """
    Stores a single contact us entry.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"