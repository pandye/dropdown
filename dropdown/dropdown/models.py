from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.name  

class City(models.Model):
    name = models.CharField(max_length=30)
    state = models.ForeignKey(State)

    def __str__(self):
        return self.name



