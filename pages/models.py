from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    experience_years = models.IntegerField()

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.name
    
    