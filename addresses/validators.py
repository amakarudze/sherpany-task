from django.core.exceptions import ValidationError


def validate_address(address):
    if "Unnamed" in address:
        raise ValidationError("Location does not have an address and cannot be saved.")
    else:
        return address
