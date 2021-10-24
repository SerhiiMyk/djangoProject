from django.db import models
from django.core import validators as V
from apps.autopark.models import AutoParkModel


# Create your models here.

class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20, validators=[V.MinLengthValidator(2), V.MaxLengthValidator(20)])
    model = models.CharField(max_length=20, validators=[V.MinLengthValidator(2), V.MaxLengthValidator(20)])
    year = models.IntegerField(validators=[V.MinValueValidator(1980), V.MaxValueValidator(2021)])
    autopark = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
