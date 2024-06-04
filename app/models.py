from django.db import models


# Create your models here.
class Area(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    formed = models.CharField(max_length=30)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Building(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    land_area = models.FloatField()
    floor = models.IntegerField()
    parking_lot = models.BooleanField()
    playground = models.BooleanField()
    elevator = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
