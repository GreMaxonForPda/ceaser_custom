# набор символов для проверок и прочего
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = alphabet.upper()
other = "1!2@3#4$5%6^7&8*9(0)-_ +=~|,./"

full_alphabet = other + alphabet + alphabet_upper

# основная функция, ради которой и задумалось все
def encrypt(key: str, text: list, symbols: str):
    new_text = []
    key_len = len(key)

    for i, word in enumerate(text):
        key_char = key[i % key_len]
        shift = symbols.index(key_char) if key_char in symbols else 7   # сдвиг по позиции ключа в списке всех символов, иначе сдвиг равен 7

        # проход по каждому символу текста,
        # нахождение индекса позиции и добавление сдвига (с поправкой на длину списка доступных символов и на присутствие этого символа в принципе),
        # добавление этого символа в строку итогового текста
        encrypted = "".join(symbols[(symbols.index(sym) + shift) % len(symbols)] if sym in symbols else sym for sym in word)
        new_text.append(encrypted)

    return new_text

# # тест дешифровки, в будущем отдельная функция
# def decrypt(key: str, text: list):
#     start_text = 0
#     start_key = 0
#     new_text = []
#     for iterable in text:
#         text_now = ""
#         for sym in text[start_text]:
#             if sym in all_sym:
#                 sym_point = all_sym.find(sym)
#                 text_now += all_sym[sym_point - int(key[start_key]) % len(all_sym)]
#             new_text.append(text_now)
#             start_text += 1
#             start_key += 1

#     return new_text


# немного тестов
test_text = ("password", "strong password", "strong_password")
test_key = "admin0"

print(encrypt(key=test_key, text=test_text, symbols=full_alphabet))
