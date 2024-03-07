from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10)

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    is_present = models.BooleanField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
