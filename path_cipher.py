import re
from random import randint

LETTERS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФЧЦЧШЩЪЫЬЭЮЯ0123456789,.!,:; '

if __name__ == '__main__':
    k = int(input('Enter the key: '))
    type = input('Encrypt or decrypt: ')
    chars = []
    with open('path_cipher_output.txt', 'r') as myself:
        for row in myself:
            for char in row:
                chars.append(char)

    if len(chars) % (k * k) > 0:
        for i in range(k * k - len(chars) % (k * k)):
            chars.append(LETTERS[randint(0, len(LETTERS) - 1)])

    if type == 'e':
        while len(chars) // k * k > 0:
            matrix = []
            for i in range(k):
                tmp1 = i * k
                tmp2 = (i + 1) * k
                matrix.append(chars[tmp1:tmp2])
            encrypted_matrix = []
            for col in range(k):
                count = 0;
                buf = []
                for row in range(col + 1):
                    buf.append(matrix[row][col - count])
                    count += 1
                if col % 2 == 0:
                    buf.reverse()
                encrypted_matrix.extend(buf)
            print(encrypted_matrix)
            f = open("path_cipher_output.txt", "a")
            for row_elements in encrypted_matrix:
                for char in row_elements:
                    f.write('{0:s}'.format(char))
            chars = chars[k * k:len(chars)]
    else:
        block_count = 0
        while len(chars) // k * k > block_count:
            decrypted_matrix = [[None for i in range(k)] for j in range(k)]
            row = chars[block_count * k * k:(block_count + 1) * k * k]
            char_count = 0
            for diagonal_number in range(k):
                count = 0
                for j in range(diagonal_number + 1):
                    decrypted_matrix[j][diagonal_number - count] = row[char_count]
                    count += 1
                    char_count += 1
            for diagonal_number in range(k - 2, 0, -1):
                count = 0
                for j in range(diagonal_number + 1):
                    decrypted_matrix[k - j - 1][k - diagonal_number - count - 1] = row[char_count]
                    count += 1
                    char_count += 1
            print(decrypted_matrix)
            block_count += 1
