text = input("Введите текст: ")

count = 0
for word in text.split():
    cleaned = word.strip(".,!?;:").lower()
    if not cleaned:
        continue
    if cleaned.count("а") == 1:
        print(cleaned)
        count += 1

if count == 0:
    print("Нет совпадений")
print(f"Количество: {count}")