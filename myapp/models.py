from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(null=True,blank=True)

    def __str__(self):
        return self.title
    