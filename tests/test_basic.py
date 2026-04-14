import pytest

from basic import is_leap_year, remove_duplicates, count_vowels


@pytest.mark.parametrize(
    "year, expected",
    [
        (2000, True),
        (1900, False),
        (2024, True),
        (2023, False),
    ],
)
def test_is_leap_year(year, expected):
    assert is_leap_year(year) is expected


@pytest.mark.parametrize(
    "items, expected",
    [
        ([1, 2, 2, 3], [1, 2, 3]),
        ([], []),
        (["a", "a", "b"], ["a", "b"]),
        ([1, 1, 1, 1], [1]),
    ],
)
def test_remove_duplicates(items, expected):
    assert remove_duplicates(items) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", 2),
        ("Привет", 2),
        ("rhythm", 0),
        ("АЕЁИОУЫЭЮЯ", 10),
        ("", 0),
    ],
)
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected
