money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

i = 0
while money_capital - spend >= 0:
    if money_capital - spend >= 0:
        money_capital = money_capital + salary - spend * ((increase + 1) ** i)
        i = i+1
    else:
        i = i+2
print("Количество месяцев, которое можно протянуть без долгов:", i)