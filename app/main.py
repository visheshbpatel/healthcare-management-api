from models.address import Address
from models.emergency_contact import EmergencyContact
from models.patient import Patient
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

patient = Patient(
    first_name="Vishesh",
    last_name="Patel",
    date_of_birth="2004-03-12",
    gender=Gender.MALE,
    email="vbp@gmail.com",
    phone_number="499499499",
    blood_group=BloodGroup.A_POSITIVE,
    height_cm=183,
    weight_kg=65,
    occupation="Student",
    address=address,
    emergency_contact=emergency_contact
)


print(patient)
