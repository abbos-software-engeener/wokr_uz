from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import EmailField


class Shipper(models.Model):
    truck_type = models.CharField(max_length=250)

    def __str__(self):
        return self.truck_type


class OurService(models.Model):
    type = models.ForeignKey(Shipper,on_delete=models.RESTRICT)
    title = models.CharField(max_length=50)
    icon = models.ImageField()
    description = models.TextField()


# class Comment(models.Model):
#     parent = models.ForeignKey('Comment', null=True, default=None, on_delete=models.RESTRICT,related_name="%(class)s_parent")
#     user = models.ForeignKey(User, default=None, on_delete=models.RESTRICT)
#     comment = models.TextField(verbose_name="izoh")
#     image = models.ImageField(upload_to="comment/", null=True, default=None, blank=True)
#     like = models.CharField(max_length=100, default=0)
#     dislike = models.CharField(max_length=100, default=0)
#     added_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#

class Carrier(models.Model):
    truckload_type = models.ForeignKey(Shipper, on_delete=models.RESTRICT)
    name = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    pick_up = models.DateField()
    delivery_date = models.DateField()
    phone_number = models.IntegerField(default=12)
    email = models.EmailField(default="example@gmail.com")
    from_city = models.CharField(max_length=250, default="state/city")
    to_sity = models.CharField(max_length=250, default="state/city")
    comments = models.TextField()

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return self.title


class Career(models.Model):
    posion = models.CharField(max_length=250)
    time = models.CharField(max_length=250, default="07:00-21:00")
    payment = models.FloatField()
    company = models.CharField(max_length=250)
    phone_number = models.IntegerField(default=12)
    email = EmailField(default="example@gmail.com")
    location = models.CharField(max_length=250)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    icon = models.ImageField(upload_to='uploads/%Y/%m/%')
    description = models.TextField()

    def __str__(self):
        return self.posion


class ContactUser(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField(default=12)
    email = models.EmailField()
    comments = models.TextField()


    def __str__(self):
        return self.name