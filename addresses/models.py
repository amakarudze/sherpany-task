from django.db import models, IntegrityError


class Address(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    address = models.CharField(max_length=255)

    class Meta:
        managed = True

    def __str__(self):
        return self.address

    @classmethod
    def create(cls, lat, lng, address):
        if "Unnamed Road" in address:
            raise ValueError("Location does not have an address")
        elif Address.objects.filter(address__iexact=address).exists():
            raise IntegrityError("That address already exists in the database")
        else:
            new_address = cls(lat=lat, lng=lng, address=address)
        return new_address
