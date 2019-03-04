if __name__ == '__main__':
    message = input('Enter the message: ')
    key = input('Enter the key: ')
    mode = input('Encrypt or decrypt: ')

    LETTERS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФЧЦЧШЩЪЫЬЭЮЯ0123456789,.!,:; '

    key_len = len(key)
    letters_len = len(LETTERS)

    translated = ''

    message = message.upper()

    for i, symbol in enumerate(message):
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            key_num = LETTERS.find(key[i % key_len])
            if mode == 'encrypt':
                num = (num + key_num) % letters_len
            elif mode == 'decrypt':
                num = (num - key_num) % letters_len
            translated = translated + LETTERS[num]
        else:
         translated = translated + symbol

    print(translated)
