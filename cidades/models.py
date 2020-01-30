from django.db import models
from django.contrib.gis.db import models as geomodels

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    geometry = geomodels.PointField()

    class Meta:
        # order of drop-down list items
        ordering = ('name',)

        # plural form in admin view
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return f'{self.name} {self.id}'
    
