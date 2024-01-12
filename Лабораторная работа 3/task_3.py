# TODO  Напишите функцию count_letters
def count_letters(str_1):
    letters = {}
    str_1 = str_1.lower()
    for letter in str_1:
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters


#TODO Напишите функцию calculate_frequency

def calculate_frequency(letters):
    suma = sum(letters.values())
    chastoty = {}
    for bukva, kol in letters.items():
        from decimal import Decimal
        num = Decimal(kol / suma)
        chastota = round(num, 2)
        chastoty[bukva] = chastota
    return chastoty


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

step_1 = count_letters(main_str)
step_2 = calculate_frequency(step_1)

for step_1, step in step_2.items():
    print(f"{step_1}: {step}")
