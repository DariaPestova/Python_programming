list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
middle_part = len(list_players) // 2
left_part = list_players[:middle_part]
right_part = list_players[middle_part:]
print(left_part)
print(right_part)
