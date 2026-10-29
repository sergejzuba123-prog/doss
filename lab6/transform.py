numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

absolute = []
for number in numbers:
    if number < 0:
        absolute.append(-number)
    else:
        absolute.append(number)

print(f"Исходный список: {numbers}")
print(f"Новый список: {absolute}")