surname = input("Фамилия: ")
name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст: "))
subject = input("Любимый предмет: ")
hours_per_week = float(input("Часов подготовки в неделю: "))

if age < 1 or age > 120:
    print("Ошибка: возраст ")
    raise SystemExit(1)
if hours_per_week < 0:
    print("Ошибка: часы не могут быть отрицательными.")
    raise SystemExit(1)

full_name = f"{name} {surname}"
age_in_four_years = age + 4
hours_in_four_weeks = hours_per_week * 4
hours_per_day = hours_per_week / 7

print()
print("Карточка студента")
print(f"Полное имя: {full_name}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст: {age}")
print(f"Любимый предмет: {subject}")
print(f"Возраст через четыре года: {age_in_four_years}")
print(f"Подготовка за четыре недели: {hours_in_four_weeks:.2f} ч")
print(f"Среднее время подготовки в день: {hours_per_day:.2f} ч")