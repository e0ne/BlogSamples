from django.db import models
from django.contrib import admin

class Address(models.Model):
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Adresses"


class Person(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    address = models.ForeignKey(Address)
    

class Employee(Person):
    title = models.CharField(max_length=50)


#admin.site.register(Address)
#admin.site.register(Person)
#admin.site.register(Employee)

