from django.db import models
# Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=2083)
    image = models.ImageField(blank="False", null=True)
    class Meta:
        db_table = 'Hotels'
        # Add verbose name
        verbose_name = 'Hotel List'


class Fashon(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=2083)
    image = models.ImageField(blank="False", null=True)
    class Meta:
        db_table = 'Fashons'
        # Add verbose name
        verbose_name = 'Fashon List'


class Farm(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank="False", null=True)
    link = models.CharField(max_length=2083)
    class Meta:
        db_table = 'Agriculture'


class Market(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=2083)
    image = models.ImageField(blank="False", null=True)
    class Meta:
        db_table = 'Markets'


class WildLife(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=2083)
    image = models.ImageField(blank="False", null=True)
    class Meta:
        db_table = 'Wildlife'
    

class Office(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=2083)
    image = models.ImageField(blank="False", null=True)
    class Meta:
        db_table = 'Offices'
 

class Sport(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=2083)
    image = models.ImageField(blank="False", null=True)
    class Meta:
        db_table = 'Sports'

class School(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=2083)
    image = models.ImageField(blank="False", null=True)
    class Meta:
        db_table = 'Schools'

class News(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=2083)
    image = models.ImageField(blank="False", null=True)
    class Meta:
        db_table = 'News'

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=2083)
    image = models.ImageField(blank="False", null=True)
    class Meta:
        db_table = 'Hospitals'

class Travel(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=2083)
    image = models.ImageField(blank="False", null=True)
    class Meta:
        db_table = 'Travel'
