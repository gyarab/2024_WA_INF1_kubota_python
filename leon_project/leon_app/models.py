from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='projects/thumbnail', null=True, blank=True)
    short_desc = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    created = models.DateField()

class Feedback(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='feedbacks')
    name = models.CharField(max_length=50)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)