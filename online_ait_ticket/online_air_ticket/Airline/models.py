from django.db import models

# Create your models here.
gender_choice= (("M",('male')),
                ('F',('female')))

class Connection(models.Model):
    place_of_origin = models.CharField(max_length=100, db_index=True, unique=True)
    place_of_destination = models.CharField(max_length=100, db_index=True, unique=True)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    date = models.DateField()
    price=models.FloatField()
    no_of_seats = models.IntegerField()
    flight_number = models.CharField(max_length=64)


class Feedback(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    feedback = models.TextField()


class Passangers(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=3, choices=gender_choice,default='male ')
    birthdate = models.DateField()
    nationality = models.CharField(max_length=100)
    flight_id = models.CharField(max_length=64)
