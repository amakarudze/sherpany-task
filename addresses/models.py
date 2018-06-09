from django.db import models


class Address(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    address = models.CharField(max_length=255)

    class Meta:
        managed = True

    def __str__(self):
        return self.address
