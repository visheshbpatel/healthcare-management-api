from typing import Annotated

from pydantic import BaseModel, Field


class EmergencyContact(BaseModel):

    name:Annotated[str,Field(min_length=3, max_length=40)]
    relationship:Annotated[str,Field(min_length=3, max_length=20)]
    phone_number:Annotated[str,Field(min_length=8, max_length=15)]