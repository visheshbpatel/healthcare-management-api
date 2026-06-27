from typing import Annotated
from datetime import date

from pydantic import BaseModel, Field, EmailStr

from enums.gender import Gender
from enums.blood_group import BloodGroup
from models.address import Address
from models.emergency_contact import EmergencyContact



class Patient(BaseModel):

    first_name:Annotated[str,Field(min_length=3, max_length=20, description="user's first name")]
    last_name:Annotated[str,Field(min_length=3, max_length=20, description="user's last name")]
    date_of_birth:date
    gender:Gender
    email:EmailStr
    phone_number:Annotated[str,Field(min_length=8, max_length=20)]
    blood_group:BloodGroup
    height_cm:Annotated[float,Field(gt=0)]
    weight_kg:Annotated[float,Field(gt=0)]
    occupation:Annotated[str|None,Field(min_length=3, max_length=20, default=None)]
    address:Address
    emergency_contact:EmergencyContact