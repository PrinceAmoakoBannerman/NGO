from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=32, default="Active")
    date_joined = models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=20, blank=True)  

    def __str__(self):
        return self.user.username

class Donation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    message = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.donor.username} - {self.amount}"

class Event(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=128)

    def __str__(self):
        return self.name

