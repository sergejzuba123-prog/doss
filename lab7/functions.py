def sum_digits(number):
    """Сумма цифр модуля целого числа. Для 0 → 0."""
    number = abs(number)
    if number == 0:
        return 0
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


def average(numbers):
    """Среднее списка либо None, если список пуст. Список не меняется."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    """Нижний регистр, без пробелов по краям, один пробел между словами."""
    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):
    """Вариант 8: новый список чисел с |x| <= threshold. Порядок и повторы сохраняются."""
    selected = []
    for number in numbers:
        if abs(number) <= threshold:
            selected.append(number)
    return selected