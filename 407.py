from math import log


def f(c, t, x):
	return c * x * log(x, 2) <= t
	
	
def binary_search(c, t):
	l = 0
	r = 1000000
	i = 0
	while i < 100:
		mid = (l + r) / 2
		if f(c, t, mid):
			l = mid
		else:
			r = mid
		i += 1
	return (l + r) / 2
	
	
if __name__ == '__main__':
	c, t = map(int, input().split())
	print('%.10f' % binary_search(c, t))