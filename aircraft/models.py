from django.db import models
from django.core import validators as V


# Create your models here.

class AircraftModel(models.Model):
    class Meta:
        db_table = 'aircrafts'

    brand = models.CharField(max_length=20, validators=[V.MinLengthValidator(2), V.MaxLengthValidator(20)])
    model = models.CharField(max_length=20,validators=[V.MinLengthValidator(2), V.MaxLengthValidator(20)])
    year = models.IntegerField(validators=[V.MinValueValidator(1980), V.MaxValueValidator(2021)])
    max_speed_km_h = models.IntegerField(validators=[V.MinValueValidator(800), V.MaxValueValidator(1100)])
    lifting_tones = models.IntegerField(validators=[V.MinValueValidator(20), V.MaxValueValidator(700)])
    wingspan_meters = models.IntegerField(validators=[V.MinValueValidator(20), V.MaxValueValidator(100)])
