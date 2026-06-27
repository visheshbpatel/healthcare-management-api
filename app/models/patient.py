from typing import Annotated
from datetime import date

from pydantic import BaseModel, Field, EmailStr, field_validator

from enums.gender import Gender
from enums.blood_group import BloodGroup
from models.address import Address
from models.emergency_contact import EmergencyContact


class Patient(BaseModel):

    @field_validator("first_name")
    @classmethod
    def validate_first_name(cls, value:str):

        if value.strip() == "":
            raise ValueError("first name can not be empty")

        return value.strip()


    @field_validator("last_name")
    @classmethod
    def validate_last_name(cls, value:str):

        if value.strip() == "":
            raise ValueError("last name can not be empty")

        return value.strip()
    

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