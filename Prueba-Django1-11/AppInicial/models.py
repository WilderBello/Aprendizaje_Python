from django.db import models

from Prueba.AppInicial.utils import image_upload_location

# Create your models here.


class Company(models.Model):
    name = models.CharField('Name', max_length=50)
    tax_number = models.IntegerField('Tax number', unique=True)


class Beer(models.Model):

    COLOR_CHOICES = (
        (1, "yellow"),
        (2, "black"),
        (3, "amber"),
        (4, "brown"),
    )

    name = models.CharField('Name', max_length=50)
    dato = models.DecimalField(
        'Titulo de dato', max_digits=5, decimal_places=2, default=0)
    is_filtered = models.BooleanField('Is filtered?', default=False)
    color = models.PositiveSmallIntegerField(
        'Color', choices=COLOR_CHOICES, default=1)
    image = models.ImageField(
        "Image", blank=True, null=True, upload_to=image_upload_location)
    Company = models.ForeignKey(Company, related_name='beers')
