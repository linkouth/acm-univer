from heapq import heappush, _siftup, nsmallest

def find_by_index(heap, idx):
	'''
		find node index by queue of input
	'''
	for i in range(len(heap)):
		if heap[i][1] == idx:
			return i

if __name__ == '__main__':
	heap = []
	n = int(input())

	for i in range(n):
		operation = input()
		if operation[0] == 'A':
			arg = int(operation[4:(len(operation) - 1)])
			heappush(heap, (arg, i + 1))
		elif operation[0] == 'D':
			arg = int(operation[4:(len(operation) - 1)])
			idx = find_by_index(heap, arg)
			heap[idx], heap[len(heap) - 1] = heap[len(heap) - 1], heap[idx]
			del heap[len(heap) - 1]
			_siftup(heap, idx)
		else:
			arg = int(operation[5:(len(operation) - 1)])
			print(nsmallest(arg, heap)[0][0])
