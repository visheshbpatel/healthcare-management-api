from models.address import Address
from models.emergency_contact import EmergencyContact
from enums.gender import Gender
from enums.blood_group import BloodGroup


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
    phone_number="599599599"
)

gender = Gender.MALE

blood_group = BloodGroup.A_POSITIVE


print(address)
print(emergency_contact)
print(gender)
print(blood_group)
