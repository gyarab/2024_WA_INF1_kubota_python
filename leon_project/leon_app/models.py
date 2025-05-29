from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='projects/thumbnail', null=True, blank=True)
    short_desc = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    created = models.DateField()

class Post(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

class Feedback(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='feedbacks')
    name = models.CharField(max_length=50, blank=True)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.user.username