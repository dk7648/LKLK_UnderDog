from django.contrib import admin

# Register your models here.
from commentapp.models import Comment
from projectapp.models import Project

admin.site.register(Project)
admin.site.register(Comment)