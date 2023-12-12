users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
dict_ = {
"Общее количество" : 0,
"Уникальные посещения" : 0
}
num_1 = len(users)
uniq_ = set(users)
num_2 = len(uniq_)

dict_ = {
"Общее количество" : num_1,
"Уникальные посещения" : num_2
}
print(dict_)