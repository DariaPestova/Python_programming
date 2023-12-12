# TODO Найдите количество книг, которое можно разместить на дискете


memory_capacity = 1.44 #Мб
number_of_pages = 100
number_of_lines = 50
number_of_symbols = 25
code_weight = 4 #байта
book_weight = code_weight * number_of_symbols * number_of_lines * number_of_pages  / (1024 **2)
number_of_books = int(memory_capacity // book_weight)
print("Количество книг, помещающихся на дискету:", number_of_books)

