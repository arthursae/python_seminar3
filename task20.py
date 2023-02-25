# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход
# подается только одно слово, которое содержит либо только английские, либо только русские буквы.
#
# *Пример:*
#
# ноутбук
#     12

def calc_score(word, score_data) -> int:
    score = 0
    if len(word) > 1:
        for letter in word:
            for (scores, letters) in score_data.items():
                if letter in letters:
                    score += scores
        return score
    else:
        return 0


def is_valid_language(word, alphabet_range):
    (lowercase1, lowercase2, uppercase1, uppercase2) = alphabet_range
    result = []
    for letter in word:
        if lowercase1 <= letter <= lowercase2 or uppercase1 <= letter <= uppercase2 or letter == ' ' or letter == '-':
            result.append(False)
        else:
            result.append(True)
    return not any(result)


en = {1: ('a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r'),
      2: ('d', 'g'),
      3: ('b', 'c', 'm', 'p'),
      4: ('f', 'h', 'v', 'w', 'y'),
      5: ('k',),
      8: ('j', 'x'),
      10: ('q', 'z')}

ru = {1: ('а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'),
      2: ('д', 'к', 'л', 'м', 'п', 'у'),
      3: ('б', 'г', 'ё', 'ь', 'я'),
      4: ('й', 'ы'),
      5: ('ж', 'з', 'х', 'ц', 'ч'),
      8: ('ш', 'э', 'ю'),
      10: ('ф', 'щ', 'ъ')}

word = input('Введите слово: ')
russian = english = False

if is_valid_language(word, ('а', 'я', 'А', 'Я')):
    russian = True
elif is_valid_language(word, ('a', 'z', 'A', 'Z')):
    english = True

if russian:
    word = word.lower().encode()
    word = word.decode()
    total_score = calc_score(word, ru)
elif english:
    word = word.lower()
    total_score = calc_score(word, en)
else:
    print('Разрешаются либо только английские, либо только русские буквы')

if russian or english:
    print(word, '->', total_score)
