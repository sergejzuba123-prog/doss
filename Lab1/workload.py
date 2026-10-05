subject1 = input("Название первого предмета: ")
lessons1 = int(input("Количество занятий по первому предмету за неделю: "))
duration1 = int(input("Продолжительность занятия первого предмета (мин): "))

subject2 = input("Название второго предмета: ")
lessons2 = int(input("Количество занятий по второму предмету за неделю: "))
duration2 = int(input("Продолжительность занятия второго предмета (мин): "))

available_hours = float(input("Доступное время на неделю (часы): "))

if lessons1 < 0 or lessons2 < 0:
    print("Ошибка: количество занятий не может быть отрицательным.")
    raise SystemExit(1)
if duration1 <= 0 or duration2 <= 0:
    print("Ошибка: продолжительность занятия должна быть положительной.")
    raise SystemExit(1)

minutes1 = lessons1 * duration1
minutes2 = lessons2 * duration2
total_minutes = minutes1 + minutes2
total_hours = total_minutes / 60

if available_hours < total_hours:
    print("Ошибка: доступное время меньше суммарной нагрузки.")
    raise SystemExit(1)

free_hours = available_hours - total_hours
four_weeks_hours = total_hours * 4

print()
print("Учебная нагрузка")
print(f"{subject1}: {minutes1} мин")
print(f"{subject2}: {minutes2} мин")
print(f"Общая нагрузка: {total_minutes} мин = {total_hours:.2f} ч")
print(f"Остаток свободного времени: {free_hours:.2f} ч")
print(f"Нагрузка за четыре недели: {four_weeks_hours:.2f} ч")