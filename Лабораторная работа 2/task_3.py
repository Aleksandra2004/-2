def count_letters(text):
    letter_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return {k: v for k, v in letter_count.items() if k.islower()}


def calculate_frequency(letter_counts):
    total_letters = sum(letter_counts.values())
    frequencies = {}
    for letter, count in letter_counts.items():
        frequencies[letter] = format(count / total_letters, '.2f')
    return frequencies

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

letters_count = count_letters(main_str)
letter_frequencies = calculate_frequency(letters_count)

for letter, frequency in letter_frequencies.items():
    print(f"{letter}: {frequency}")