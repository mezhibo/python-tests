def is_leap_year(year: int) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def remove_duplicates(items: list) -> list:
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


def count_vowels(text: str) -> int:
    vowels = "аеёиоуыэюяaeiou"
    return sum(1 for ch in text.lower() if ch in vowels)
