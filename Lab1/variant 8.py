order_name = input("Название заказа: ")
customer_name = input("Имя заказчика: ")

item1_name = input("Название первой позиции: ")
item1_qty = int(input("Количество первой позиции: "))
item1_price = float(input("Цена единицы первой позиции: "))

item2_name = input("Название второй позиции: ")
item2_qty = int(input("Количество второй позиции: "))
item2_price = float(input("Цена единицы второй позиции: "))

delivery = float(input("Стоимость доставки: "))
paid = float(input("Внесённая сумма: "))

if item1_qty < 0 or item2_qty < 0:
    print("Ошибка: количество не может быть отрицательным.")
    raise SystemExit(1)
if item1_price < 0 or item2_price < 0 or delivery < 0:
    print("Ошибка: цена и доставка не могут быть отрицательными.")
    raise SystemExit(1)

cost1 = item1_qty * item1_price
cost2 = item2_qty * item2_price
goods_total = cost1 + cost2
grand_total = goods_total + delivery
total_qty = item1_qty + item2_qty

if paid < grand_total:
    print("Ошибка: внесённой суммы недостаточно.")
    raise SystemExit(1)

change = paid - grand_total

print(f"=== Заказ: {order_name} ===")
print(f"Заказчик: {customer_name}")
print(f"{item1_name} | {item1_qty} | {item1_price:.2f} | {cost1:.2f}")
print(f"{item2_name} | {item2_qty} | {item2_price:.2f} | {cost2:.2f}")
print(f"Стоимость товаров без доставки: {goods_total:.2f} руб.")
print(f"Доставка: {delivery:.2f} руб.")
print(f"Итоговая сумма с доставкой: {grand_total:.2f} руб.")
print(f"Общее количество единиц: {total_qty}")
print(f"Сдача: {change:.2f} руб.")