from functions import average, normalize_text, select_numbers, sum_digits

# --- Базовые проверки (из задания) ---
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

# --- Проверки варианта 8: |x| <= threshold ---

# Контрольный набор
assert select_numbers([-5, 0, 2, 5], 2) == [0, 2]

# Пустой список
assert select_numbers([], 2) == []
assert select_numbers([], 0) == []

# Граница условия: |x| == threshold включается
assert select_numbers([-2, 2, 3, -3], 2) == [-2, 2]
assert select_numbers([0], 0) == [0]

# Рядом с границей: |x| = 3 > 2 — не подходит
assert select_numbers([3, -3], 2) == []

# Все подходят
assert select_numbers([-1, 0, 1], 2) == [-1, 0, 1]

# Все не подходят
assert select_numbers([-10, 10], 2) == []

# Повторы сохраняются
assert select_numbers([2, 2, -2, 3, 2], 2) == [2, 2, -2, 2]

# Исходный список не изменяется
original = [-5, 0, 2, 5]
saved = original.copy()
select_numbers(original, 2)
assert original == saved

# Дробное среднее — сравнение с допуском
actual = average([1, 2])
assert abs(actual - 1.5) < 1e-9

print("Базовые проверки и проверки варианта пройдены")