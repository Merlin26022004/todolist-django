from django.db import models

class loginForm(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title