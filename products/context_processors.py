from .models import OwnerContact

def owner_contact(request):
    owner_contact = OwnerContact.objects.first()
    return {'owner_contact':owner_contact}