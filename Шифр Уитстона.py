from collections import OrderedDict


if __name__ == '__main__':
	alph = [chr(i) for i in range(1072, 1103 + 1)]
	alph.extend([',', '.', ';', ':', ' ', '!'])

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

	first_matrix = [[] for i in range(row_number)]

	for i in key:
		first_matrix[0].append(i)
	count = 0
	# while count < alph_size - key_size:
	for i in range(1, row_number - 1):
		for j in range(key_size):
			first_matrix[i].append(tmp_alph[count])
			count += 1
	full_column_number = len(tmp_alph) - count
	while count < len(tmp_alph):
		first_matrix[row_number - 1].append(tmp_alph[count])
		count += 1

	first_matrix_as_list = list()
	for item in list(first_matrix):
		first_matrix_as_list.extend(item)

	second_matrix = [[] for i in range(row_number)]
	for i in range(row_number - 1):
		for j in range(key_size):
			second_matrix[i].append(None)
	for i in range(full_column_number):
		second_matrix[row_number - 1].append(None)

	count = 0
	for i in range(full_column_number):
		for j in range(row_number):
			second_matrix[j][i] = first_matrix_as_list[count]
			count += 1
	for i in range(full_column_number, key_size):
		for j in range(row_number - 1):
			second_matrix[j][i] = first_matrix_as_list[count]
			count += 1

	for row in first_matrix:
		for char in row:
			print(char, end=' ')
		print()


	for row in second_matrix:
		for char in row:
			print(char, end=' ')
		print()
