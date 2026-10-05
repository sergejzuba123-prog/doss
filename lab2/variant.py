total = int(input("Общее количество заданий: "))
capacity = int(input("Сколько заданий в одном комплекте: "))

full_units = total // capacity
remainder = total % capacity

# Минимальное число комплектов (округление вверх), с учётом случая total == 0
min_units = 0 if total == 0 else (total + capacity - 1) // capacity

print(f"Полностью заполненных комплектов: {full_units}")
print(f"Заданий осталось (не вошло в полный комплект): {remainder}")
print(f"Минимальное число комплектов для всех заданий: {min_units}")
