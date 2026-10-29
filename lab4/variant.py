n = int(input("Введите n >= 0: "))

count = 0
total = 0

for i in range(n):
    value = int(input(f"Число {i + 1}: "))
    if abs(value) > 5:
        count += 1
        total += value

print(f"Количество: {count}")
print(f"Сумма: {total}")