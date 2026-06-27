from typing import Annotated
from datetime import date

from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator, computed_field

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
    

    @model_validator(mode="after")
    def validate_date_of_birth(self):

        if self.date_of_birth > date.today():
            raise ValueError("Date of birth can't be in future")
        
        return self
    

    @computed_field
    @property
    def bmi(self)->float:

        height = self.height_cm/100
        bmi = round(self.weight_kg/((height)**2),2)
        return bmi
    

    @computed_field
    @property
    def age(self)->int:

        today = date.today()

        age = today.year - self.date_of_birth.year

        if  (today.month, today.day) < (
            self.date_of_birth.month, self.date_of_birth.day
            ):
            age-=1

        return age
    

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


