from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Feed(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='feed', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='feed/', null=False)
    content = RichTextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)