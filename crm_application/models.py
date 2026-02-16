from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Subscription(models.Model):
    type = models.CharField(max_length=255)
    cost = models.FloatField()
    createdDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.type



class Address(models.Model):
    address = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.city + ' ' + self.zip

class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    createdDate = models.DateTimeField(default=timezone.now)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='subscription_set')

    def __str__(self):
        return self.firstname + ' ' + self.lastname

class Card(models.Model):
    holder = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    expiry = models.CharField(max_length=255)
    createdDate = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_card")

    def __str__(self):
        return self.number
    
class Bill(models.Model):
    status = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    amount = models.FloatField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='address_set')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_bill')
    def __str__(self):
        return self.status


class Lead(models.Model):
    status = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_set')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='lead_address')
    createdDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Project(models.Model):
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    notes = models.TextField()
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE,          related_name='project_subscription')
    createdDate = models.DateTimeField(default=timezone.now)
    releaseDate = models.DateTimeField()
    budget = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_set')
    assignedTo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned')

    def __str__(self):
        return self.name
    