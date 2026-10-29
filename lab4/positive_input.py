rejected = 0
number = int(input("Введите положительное целое: "))

while number <= 0:
    rejected += 1
    number = int(input("Не подходит. Введите положительное целое: "))

print(f"Квадрат: {number * number}")
print(f"Отклонено попыток: {rejected}")