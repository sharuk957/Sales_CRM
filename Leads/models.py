from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=250)
    product_code = models.IntegerField()
    price = models.FloatField()
    tax = models.FloatField()
    units = models.IntegerField()

    def __str__(self):
        return self.name

class Person(models.Model):

    name = models.CharField(max_length=250)
    owner = models.CharField(max_length=250)
    owner_email = models.EmailField()
    mobile_num = ArrayField(models.CharField(max_length=10,blank=True),null=True)
    email = ArrayField(models.CharField(max_length=55,blank=True),null=True)

    def __str__(self):
        return self.name