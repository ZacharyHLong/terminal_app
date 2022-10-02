import exceptions as ex
import pytest
from unittest.mock import patch


# check that get_a_name function accepts alphabetic characters and converts it to title case
def test_get_a_name_RightDataType(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'zac')
    i = ex.get_a_name("What is the player's first name?")
    assert i == 'Zac'

# check that the get_a_number function accepts a numerical value of the right amount of digits
def test_get_a_number_RightDataType(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '24')
    i = ex.get_a_number("What is the player's jersey number?", 1, 2)
    assert i == '24'
