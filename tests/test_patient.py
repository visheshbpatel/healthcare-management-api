from datetime import date, timedelta

import pytest
from pydantic import ValidationError

from tests.helpers import create_test_patient


def test_create_valid_patient():
    patient = create_test_patient()

    assert patient.first_name == "Vishesh"


def test_future_date_of_birth_raises_validation_error():
    future_date = date.today() + timedelta(days=1)

    with pytest.raises(ValidationError):
        create_test_patient(date_of_birth=future_date)


def test_blank_first_name_raises_validation_error():
    with pytest.raises(ValidationError):
        create_test_patient(first_name="     ")


def test_bmi_is_calculated_correctly():
    patient = create_test_patient()

    assert patient.bmi == 19.41


def test_age_is_calculated_correctly():
    patient = create_test_patient()

    assert patient.age == 22