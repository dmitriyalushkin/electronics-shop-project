"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item1():
    """Создаем экземпляр1 класса в фикстуре"""
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item2():
    """Создаем экземпляр2 класса в фикстуре"""
    return Item("Ноутбук", 20000, 5)


def test_apply_discount(item1, item2):
    Item.pay_rate = 1.0
    item1.apply_discount()
    item2.apply_discount()
    assert item1.price == 10000.0
    assert item2.price == 20000.0


def test_calculate_total_price(item1, item2):
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


