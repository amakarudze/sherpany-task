from django.core.exceptions import ValidationError


def validate_address(location):
    if "Unnamed" in location:
        raise ValidationError("Location does not have an address")
    else:
        return location
