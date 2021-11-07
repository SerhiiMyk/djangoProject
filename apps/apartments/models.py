from django.core import validators as V
from django.db import models

from apps.profile.models import ProfileModel

# Create your models here.


class ApartmentsModel(models.Model):
    class Meta:
        db_table = 'apartments'

    name = models.CharField(max_length=20, validators=[V.MinLengthValidator(2), V.MaxLengthValidator(20)])
    country = models.CharField(max_length=20, validators=[V.MinLengthValidator(2), V.MaxLengthValidator(20)])
    city = models.CharField(max_length=20, validators=[V.MinLengthValidator(2), V.MaxLengthValidator(20)])
    district = models.CharField(max_length=20, validators=[V.MinLengthValidator(2), V.MaxLengthValidator(20)])
    street = models.CharField(max_length=20, validators=[V.MinLengthValidator(2), V.MaxLengthValidator(20)])
    area = models.IntegerField(validators=[V.MinValueValidator(5), V.MaxValueValidator(1000)])
    guests = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(10)])
    beds = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(20)])
    type = models.CharField(max_length=20, validators=[V.MinLengthValidator(2), V.MaxLengthValidator(10)])
    price = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(100000)])
    check_in = models.DateField()
    check_out = models.DateField()
    photo = models.ImageField(upload_to='photo', blank=True)
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='apartments')
