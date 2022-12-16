per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Сумма, которую вы планируете положить под проценты - "))

deposit = []
for value in per_cent:
    deposit.append(int(per_cent[value]*money/100))
print(deposit)
max_deposit = max(deposit)
print('Максимальная сумма, которую вы можете заработать - '+ str(max_deposit))
