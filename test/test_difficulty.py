import pytest
from src.difficulty import parse_difficulty, Difficulty, ATTEMPTS

def test_parse_numeric_inputs():
    assert parse_difficulty("1") == Difficulty.EASY
    assert parse_difficulty("2") == Difficulty.MEDIUM
    assert parse_difficulty("3") == Difficulty.HARD

def test_parse_text_inputs():
    assert parse_difficulty("easy") == Difficulty.EASY
    assert parse_difficulty("facile") == Difficulty.EASY
    assert parse_difficulty("medium") == Difficulty.MEDIUM
    assert parse_difficulty("medio") == Difficulty.MEDIUM
    assert parse_difficulty("hard") == Difficulty.HARD
    assert parse_difficulty("difficile") == Difficulty.HARD

def test_invalid_input():
    with pytest.raises(ValueError):
        parse_difficulty("banana")

def test_attempts_constant():
    assert ATTEMPTS == 10
