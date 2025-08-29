alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = alphabet.upper()
other = "1!2@3#4$5%6^7&8*9(0)-_+=~|,./"

all_sym = alphabet + alphabet_upper + other

def encrypt(key: str, text: list):
    start_text = 0
    start_key = 0
    new_text = []
    for iterable in text:
        text_now = ""
        for sym in text[start_text]:
            if sym in all_sym:
                sym_point = all_sym.find(sym)
                text_now += all_sym[sym_point + int(key[start_key]) % len(all_sym)]
            new_text.append(text_now)
            start_text += 1
            start_key += 1

    return(new_text)

def decrypt(key: str, text: list):
    start_text = 0
    start_key = 0
    new_text = []
    for iterable in text:
        text_now = ""
        for sym in text[start_text]:
            if sym in all_sym:
                sym_point = all_sym.find(sym)
                text_now += all_sym[sym_point - int(key[start_key]) % len(all_sym)]
            new_text.append(text_now)
            start_text += 1
            start_key += 1

    return(new_text)


first = encrypt(key="79598499640", text=("password"))
second = decrypt(key="79598499640", text="".join(f'{some}' for some in first))

print(second)
