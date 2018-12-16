def quick_sort(arr, l, r):
	i, j = l, r
	x = arr[(l + r) // 2]
	while i <= j:
		while arr[i] < x:
			i += 1
		while x < arr[j]:
			j -= 1
		if i <= j:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
			j -= 1
	if l < j:
		quick_sort(arr, l, j)
	if i < r:
		quick_sort(arr, i, r)
		

def sum(a, b, x):
	i = 0
	j = len(b) - 1
	while a[i] + b[j] != x and i != len(a) - 1 and j != 0:
		while j > 0 and a[i] + b[j] > x:
			j -= 1
		while i < len(a) - 1 and a[i] + b[j] < x:
			i += 1
	while j > 0 and a[i] + b[j] > x:
		j -= 1
	while i < len(a) - 1 and a[i] + b[j] < x:
		i += 1
	if a[i] + b[j] == x:
		return True
	return False
		
		
if __name__ == '__main__':
	n = int(input())
	a = []
	a = list(map(int, input().split()))
	m = int(input())
	b = []
	b = list(map(int, input().split()))
	k = int(input())
	c = []
	c = list(map(int, input().split()))
	quick_sort(a, 0, n - 1)
	quick_sort(b, 0, m - 1)
	for i in range(k):
		if sum(a, b, c[i]):
			print('YES')
		else:
			print('NO')
