money = int(input("Введите сумму вклада:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for key in per_cent:
    [deposit.append(money * per_cent[key] / 100)]

deposit_int = list(map(int, deposit))

print("deposit =", deposit_int)
print("Максимальная сумма, которую вы можете заработать —", max(deposit_int))