import json as js


with open("data.json", "r", encoding="utf-8") as f:
    data = js.load(f)

full_alphabet = data["alphabet"] + data["other"]


# основная функция, ради которой и задумалось все
def encrypt(key: str, text: list, symbols: str):
    new_text = list()
    key_len = len(key)

    for i, word in enumerate(text):
        key_char = key[i % key_len]
        # сдвиг по позиции ключа в списке всех символов, иначе сдвиг равен 7
        shift = symbols.index(key_char) if key_char in symbols else 7

        '''
        проход по каждому символу текста,
        нахождение индекса позиции и добавление сдвига ->
        (с поправкой на длину списка доступных символов и ->
        на присутствие этого символа в принципе), ->
        добавление этого символа в строку итогового текста
        '''
        encrypted = "".join(
            symbols[(symbols.index(sym) + shift) % len(symbols)]
            if sym in symbols else sym for sym in word)
        new_text.append(encrypted)

    return new_text


# немного тестов
test_text = ("password", "strong password", "strong_password")
test_key = "admin0"

print(encrypt(key=test_key, text=test_text, symbols=full_alphabet))
