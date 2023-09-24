import pytest
from src.keyboard import KeyBoard


@pytest.fixture
def kb():
    """Создаем экземпляр класса в фикстуре"""
    return KeyBoard('Dark Project KD87A', 9600, 5)


def test_str(kb):
    assert str(kb) == "Dark Project KD87A"


def test_language_property(kb):
    assert str(kb.language) == "EN"


def test_change_lang(kb):
    assert str(kb.change_lang()) != "RU"





