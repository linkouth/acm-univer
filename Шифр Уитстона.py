from collections import OrderedDict


if __name__ == '__main__':
	alph = [chr(i) for i in range(1072, 1103 + 1)]
	alph.extend([',', '.', ';', ':', ' '])

	alph_size = len(alph)
	# key = input('Введите ключ ').lower()
	key = 'ключ'
	key = list(OrderedDict.fromkeys(key))
	key_size = len(key)
	row_number = alph_size // key_size
	if alph_size % key_size: row_number += 1

	tmp_alph = alph
	for i in key:
		tmp_alph.remove(i)

	first_matrix = [[None for j in range(key_size)] for i in range(row_number)]
	second_matrix = [[None for j in range(key_size)] for i in range(row_number)]

	for i in range(key_size):
		first_matrix[0][i] = key[i]
	count = 0
	for i in range(1, row_number - 1):
		for j in range(key_size):
			first_matrix[i][j] = tmp_alph[count]
			count += 1

	for row in first_matrix:
		for char in row:
			print(char, end=' ')
		print()