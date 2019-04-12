from django.db import models

# Create your models here.
class Hyd_jobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=64)
    elegibility = models.CharField(max_length=64)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.CharField(max_length=12)


    def __str__(self):
        return self.title


class Blr_jobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=64)
    elegibility = models.CharField(max_length=64)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.CharField(max_length=12)

class Chennai_jobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=64)
    elegibility = models.CharField(max_length=64)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.CharField(max_length=12)

class Pune_jobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=64)
    elegibility = models.CharField(max_length=64)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.CharField(max_length=12)