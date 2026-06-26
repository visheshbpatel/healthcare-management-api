from models.address import Address
from models.emergency_contact import EmergencyContact


address = Address(
    street="599 bakers street",
    city="Indore",
    state="Madhya Pradesh",
    country="India",
    postal_code="xyz 4512",
)

emergency_contact= EmergencyContact(
    name="Madhav",
    relationship="friend",
    phone_number="599599"
)


print(address)
print(emergency_contact)
