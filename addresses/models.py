from django.db import models

from .validators import validate_address


class Address(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    location = models.CharField(max_length=255, unique=True, validators=[validate_address])

    class Meta:
        managed = True

    def __str__(self):
        return self.location
