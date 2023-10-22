from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    subject = models.IntegerField()
    password = models.IntegerField()
    team_logo = models.ImageField(null=True, blank=True, default="default.jpg")

    def __str__(self):
        return self.name


class Teams(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField()
    city = models.ManyToOneRel('Location', blank=True)

    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=50)
    teams = models.ForeignKey(Teams, on_delete=models.CASCADE)

