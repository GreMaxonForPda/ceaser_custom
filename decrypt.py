import json as js


with open("data.json", "r", encoding="utf-8") as f:
    data = js.load(f)

full_alphabet = data["alphabet"] + data["other"]


def decrypt(key: str, text: list, symbols: str):
    new_text = list()
    key_len = len(key)

    for i, word in enumerate(text):
        key_char = key[i % key_len]
        shift = symbols.index(key_char) if key_char in symbols else 7

        decrypted = "".join(
            symbols[(symbols.index(sym) - shift) % len(symbols)]
            if sym in symbols else sym for sym in word)
        new_text.append(decrypted)

    return new_text


test_text = ('QBTTXPSE', 'WXVSRK/TEWW1SVH', '67521TI3N66025Q')
test_key = "admin0"

print(decrypt(key=test_key, text=test_text, symbols=full_alphabet))
