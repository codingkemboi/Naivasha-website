from django.db import models
# Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=2083)
    image = models.ImageField(upload_to="media", null=True)
    class Meta:
        db_table = 'Hotels'
        # Add verbose name
        verbose_name = 'Hotel List'


class Fashon(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=2083)
    image = models.ImageField(upload_to="media", null=True)
    class Meta:
        db_table = 'Fashons'
        # Add verbose name
        verbose_name = 'Fashon List'


class Lake(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media", null=True)
    link = models.CharField(max_length=2083)
    class Meta:
        db_table = 'Lakes'


class Market(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=2083)
    image = models.ImageField(upload_to="media", null=True)
    class Meta:
        db_table = 'Markets'


class WildLife(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=2083)
    image = models.ImageField(upload_to="media", null=True)
    class Meta:
        db_table = 'Wildlife'
    

class Station(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=2083)
    image = models.ImageField(upload_to="media", null=True)
    class Meta:
        db_table = 'Stations'
 

class Sport(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=2083)
    image = models.ImageField(upload_to="media", null=True)
    class Meta:
        db_table = 'Sports'

class School(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=2083)
    image = models.ImageField(upload_to="media", null=True)
    class Meta:
        db_table = 'Schools'

class Trend(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=2083)
    image = models.ImageField(upload_to="media", null=True)
    class Meta:
        db_table = 'Trends'

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=2083)
    image = models.ImageField(upload_to="media", null=True)
    class Meta:
        db_table = 'Hospitals'

class Tourism(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=2083)
    image = models.ImageField(upload_to="media", null=True)
    class Meta:
        db_table = 'Tourism'
