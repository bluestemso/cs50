import pytest
from datetime import date
from seasons import calculate_minutes_lived, convert_minutes_to_words

def test_calculate_minutes_lived():
    dob = date(2023, 9, 17)
    assert calculate_minutes_lived(dob) == 527040

def test_convert_minutes_to_words():
    assert convert_minutes_to_words(527040) == "Five hundred twenty-seven thousand forty"