from django.db import models, IntegrityError


class Address(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    location = models.CharField(max_length=255)

    class Meta:
        managed = True

    def __str__(self):
        return self.location

    @classmethod
    def create(cls, lat, lng, location):
        if "Unnamed Road" in location:
            raise ValueError("Location does not have an address")
        elif Address.objects.filter(location__iexact=location).exists():
            raise IntegrityError("That address already exists in the database")
        else:
            new_address = cls(lat=lat, lng=lng, location=location)
        return new_address
