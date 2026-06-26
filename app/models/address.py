from typing import Annotated

from pydantic import BaseModel, Field


class Address(BaseModel):
    street: Annotated[str, Field(min_length=5, max_length=100)]
    city: Annotated[str, Field(min_length=2, max_length=50)]
    state: Annotated[str, Field(min_length=2, max_length=50)]
    country: Annotated[str, Field(min_length=2, max_length=50)]
    postal_code: Annotated[str, Field(min_length=3, max_length=12)]