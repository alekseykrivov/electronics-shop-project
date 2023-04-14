"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture()
def mouse():
    return Item("Мышь", 300.5, 1)
def test_name(mouse):
    assert mouse.name == 'Мышь'

def test_price(mouse):
    assert mouse.price != 300

def test_quantity(mouse):
    assert mouse.quantity == 1