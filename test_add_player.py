import exceptions as ex
import pytest
from unittest.mock import patch



def test_get_a_name_RightDataType(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'zac')
    i = ex.get_a_name("What is the player's first name?")
    assert i == 'Zac'

def test_get_a_number_RightDataType(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '24')
    i = ex.get_a_number("What is the player's jersey number?", 1, 2)
    assert i == '24'
