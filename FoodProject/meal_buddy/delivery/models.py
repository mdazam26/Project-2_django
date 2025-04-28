from django.db import models # type: ignore

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=50)


class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    picture = models.CharField(max_length=200, default="https://tse2.mm.bing.net/th/id/OIP.3JuA0-BIEyyCceG24Arr3gHaE8?rs=1&pid=ImgDetMain")
    cuisine = models.CharField(max_length=200)
    rating = models.FloatField()