
print("Фрагмент А")
# Ожидаемый результат: 5, а не строка "23".
first = "2"
second = "3"
print("Типы до преобразования:", type(first).__name__, type(second).__name__)
first_num = int(first)
second_num = int(second)
print("Типы после преобразования:", type(first_num).__name__, type(second_num).__name__)
print("Сумма:", first_num + second_num)


print("Фрагмент Б")
# Ожидаемый результат: возраст через год, при вводе 17 - 18.
age = input("Возраст: ")
print("Тип до преобразования:", type(age).__name__)
age_num = int(age)
print("Тип после преобразования:", type(age_num).__name__)
print("Возраст через год:", age_num + 1)


print("Фрагмент В")
# Ожидаемый результат: среднее 4, 7, 10 → 7.0.
first = 4
second = 7
third = 10
average = (first + second + third) / 3
print("Среднее:", average)