from django.db import models
#max and min int validators
from django.core.validators import MaxValueValidator, MinValueValidator

#create model things
class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.TextField(max_length=120, blank=False)
    quantity = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], default=0, blank=False, unique=False)

