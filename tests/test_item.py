"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest as pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def test_item():
    item = Item("Компьютер", 30000, 2)
    return item


@pytest.fixture
def test_phone():
    phone = Phone("Xiaomi", 30000, 5, 1)
    return phone


def test_item_init(test_item):
    assert test_item.name == "Компьютер"
    assert test_item.price == 30000
    assert test_item.quantity == 2


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 60000


def test_apply_discount(test_item):
    test_item.pay_rate = 0.8
    test_item.apply_discount()

    assert test_item.price == 24000.0


def test_setter(test_item):
    test_item.name = "Apple"
    assert test_item.name == "Apple"

    try:
        test_item.name = "Смартфон Apple"

    except Exception as e:
        assert e


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5


def test_repr(test_item):
    assert repr(test_item) == "Item('Компьютер', 30000, 2)"


def test_str(test_item):
    assert str(test_item) == 'Компьютер'
    # item = Item("Компьютер", 30000, 2)


def test_add(test_item, test_phone):
    assert test_item.__add__(test_phone) == 7
    phone1 = Phone("Samsung", 50000, 4, 2)
    assert test_phone.__add__(phone1) == 9
