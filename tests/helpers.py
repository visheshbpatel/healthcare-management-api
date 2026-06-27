from datetime import date

from app.models.address import Address
from app.models.emergency_contact import EmergencyContact
from app.models.patient import Patient
from app.enums.gender import Gender
from app.enums.blood_group import BloodGroup


def create_test_address():
    return Address(
        street="599 bakers street",
        city="Indore",
        state="Madhya Pradesh",
        country="India",
        postal_code="452001",
    )


def create_test_emergency_contact():
    return EmergencyContact(
        name="Madhav",
        relationship="Friend",
        phone_number="9999999999",
    )


def create_test_patient(**overrides):
    data = {
        "first_name": "Vishesh",
        "last_name": "Patel",
        "date_of_birth": date(2004, 3, 12),
        "gender": Gender.MALE,
        "email": "vbp@gmail.com",
        "phone_number": "9999999999",
        "blood_group": BloodGroup.A_POSITIVE,
        "height_cm": 183,
        "weight_kg": 65,
        "occupation": "Student",
        "address": create_test_address(),
        "emergency_contact": create_test_emergency_contact(),
    }

    data.update(overrides)

    return Patient(**data)