from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    situation = models.BooleanField(default=True)
    views = models.IntegerField(null=True)
    
    def __str__(self):
        return f"{self.title} - {self.description[:10]}"