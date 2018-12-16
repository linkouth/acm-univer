def count_sort(arr):
	result = []
	c = [-1 for _ in range(200000)]
	for i in range(len(arr)):
		c[arr[i][0] + 100000] = arr[i][1]
	for i in range(len(c)):
		if c[i] != -1:
			result.append(c[i])
	return result
	
	
if __name__ == "__main__":
	n = int(input())
	a = [[] for _ in range(200000)]
	
	for i in range(1, n + 1):
		x, y = map(int, input().split())
		a[x + 100000].append((y, i))
		
	for i in range(200000):
		if len(a[i]) != 0:
			res = count_sort(a[i])
			for j in range(len(res)):
				print(res[j], end=' ')