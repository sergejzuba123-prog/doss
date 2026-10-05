num1 = float(input("Первое число: "))
num2 = float(input("Второе число: "))
operation = input("Операция (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"{result:.2f}")
elif operation == "-":
    result = num1 - num2
    print(f"{result:.2f}")
elif operation == "*":
    result = num1 * num2
    print(f"{result:.2f}")
elif operation == "/":
    if num2 == 0:
        print("Деление на ноль запрещено")
    else:
        result = num1 / num2
        print(f"{result:.2f}")
else:
    print("Неизвестная операция")
