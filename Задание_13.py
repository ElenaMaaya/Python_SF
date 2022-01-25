ticket = int(input("Укажите количество билетов: "))
print("---")
a, b = float(990), float(1390)
sum_price_ticket = 0

for i in range(1, ticket + 1):
    age = int(input(f"Укажите возраст {i} участника конференции: "))
    if 0 <= age <= 100:
        price_ticket = a if 18 <= age <= 24 else b
        if 0 < age <= 17:
            price_ticket = 0
        print("Стоимость билета:", price_ticket, "руб.")
        print("---")
        sum_price_ticket = sum_price_ticket + price_ticket
    if age > 100 or age <= 0:
        print("Вы ввели неправильный возраст. "
              "Билет не будет учтен.")
if ticket <= 3:
    print("Сумма к оплате составляет", sum_price_ticket, "руб.")
else:
    print("Сумма к оплате со скидкой 10 % составляет",
          sum_price_ticket - (sum_price_ticket / 10), "руб.")






