from django.db import models

# Create your models here.

class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    previous_work = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
