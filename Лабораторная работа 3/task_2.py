# TODO Напишите функцию find_common_participants

def find_common_participants(str_1, str_2, n=','):
    set_1 = set(str_1.split(n))
    set_2 = set(str_2.split(n))
    inter = list(set_1.intersection(set_2))
    inter.sort()
    return inter


#TODO Провеьте работу функции с разделителем отличным от запятой

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group ))
print(find_common_participants(participants_first_group, participants_second_group, '|' ))

