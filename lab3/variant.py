value = int(input("Процент заполнения группы (0–100): "))

if value < 0 or value > 100:
    print("Ошибка диапазона")
elif 0 <= value <= 39:
    print("Есть места")
elif 40 <= value <= 79:
    print("Группа набирается")
else:  # 80–100
    print("Почти заполнена")
