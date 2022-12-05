from django.db import models
from  django.conf import settings
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class pastel(models.Model):
    tamano=models.CharField(max_length=20, blank=False, null=False)
    sabores= models.CharField(max_length=20, blank=False, null=False)
    cantidad=models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)], blank=False)
    costo= models.DecimalField(default=0,max_digits=5,decimal_places=2, blank=False)