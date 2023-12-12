salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов



i = 1
money_capital = 0
inc_ = increase + 1
while months - i >= 0:
    if months - i >= 0:
       money_capital = money_capital + spend * (inc_ ** (months - i)) - salary
       i = i + 1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital, 2))



