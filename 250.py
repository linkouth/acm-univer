def merge(a, b, c):
	n = len(a)
	m = len(b)
	iter_a = iter_b = 0
	for iter_c in range(n + m):
		if iter_a < n and (iter_b == m or a[iter_a][0] < b[iter_b][0]):
			c[iter_c] = a[iter_a]
			iter_a += 1
		elif iter_a < n and (iter_b == m or 
			a[iter_a][0] == b[iter_b][0] and a[iter_a][1] < b[iter_b][1]):
			c[iter_c] = a[iter_a]
			iter_a += 1
		else:
			c[iter_c] = b[iter_b]
			iter_b += 1
	return c
	
	
def merge_sort(a):
	if len(a) <= 1:
		return a
	l = []
	r = []
	for i in range(len(a) // 2):
		l.append(a[i])
	for i in range(len(a) // 2, len(a)):
		r.append(a[i])
	l = merge_sort(l)
	r = merge_sort(r)
	
	return merge(l, r, a)
	
	
if __name__ == '__main__':
	n = int(input())
	a = []
	for i in range(n):
		x, y = map(int, input().split())
		a.append((x, y))
	c = []
	for i in range(n):
		c.append((a[i][0], 0))
		c.append((a[i][1], 1))
		
	merge_sort(c)
	
	k = count = 0
	for i in range(2 * n):
		if c[i][1] == 0:
			count += 1
		if count > k:
			k = count
		if c[i][1] == 1:
			count -= 1
			
	count = 0
	result = 0
	start = end = 0
	for i in range(2 * n):
		if c[i][1] == 0:
			count += 1
		if k == count:
			if c[i][1] == 0:
				start = c[i][0]
		if k == count:
			if c[i][1] == 1:
				end = c[i][0]
				result += end - start + 1
		if c[i][1] == 1:
			count -= 1
	print(result)