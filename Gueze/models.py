from django.db import models
from django.utils.html import format_html
import datetime


# Create your models here.


class Verre(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    create_date = models.DateField()

    def __str__(self):
        return self.name




class srm(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " " + self.last_name


class available(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " " + self.last_name


class style(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " " + self.last_name


class Categorie(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " " + self.last_name


class bierre(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " " + self.last_name
