from functions import average, normalize_text, select_numbers, sum_digits


def main():
    number = int(input("Целое число: "))
    print(f"Сумма цифр: {sum_digits(number)}")

    numbers = []
    for part in input("Строка целых чисел через пробел: ").split():
        numbers.append(int(part))

    if average(numbers) is None:
        print("Среднее: Нет данных")
    else:
        print(f"Среднее: {average(numbers):.2f}")

    text = input("Произвольный текст: ")
    print(f"Нормализованный текст: {normalize_text(text)}")

    threshold = int(input("Порог (целое >= 0): "))
    print(f"Выборка: {select_numbers(numbers, threshold)}")


if __name__ == "__main__":
    main()