from django.db import models


class Member(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
# Create your models here.
