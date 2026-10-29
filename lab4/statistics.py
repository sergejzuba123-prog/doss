n = int(input("Введите n >= 1: "))

total = 0
positives = 0
maximum = None

for i in range(n):
    value = int(input(f"Число {i + 1}: "))
    total += value
    if value > 0:
        positives += 1
    if maximum is None or value > maximum:
        maximum = value

print(f"Сумма: {total}")
print(f"Положительных: {positives}")
print(f"Максимум: {maximum}")