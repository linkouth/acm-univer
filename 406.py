def f(s, m, p, x):
	for i in range(m):
		s += s * p / 100 - x
	return s
	

def binary_search(s, m, p, l, r):
	i = 0
	while i < 100:
		mid = (l + r) / 2
		if f(s, m, p, mid) >= 0:
			l = mid
		else:
			r = mid
		i += 1
		
	return (l + r) / 2
	
	
if __name__ == '__main__':
	s, m, p = map(int, input().split())
	l = 0
	r = (s * p / 100) + s
	print('%.7f' % binary_search(s, m, p, l, r))