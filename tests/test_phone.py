import pytest as pytest

from src.phone import Phone


@pytest.fixture
def test_phone():
    phone = Phone("Xiaomi", 30000, 5, 2)
    return phone


def test_repr(test_phone):
    assert repr(test_phone) == "Phone('Xiaomi', 30000, 5, 2)"


def test_setter(test_phone):
    test_phone.number_of_sim = 3
    assert test_phone.number_of_sim == 3

    try:
        test_phone.number_of_sim = 2.5

    except ValueError as e:
        assert e
