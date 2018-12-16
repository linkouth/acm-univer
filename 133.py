from heapq import nsmallest, heappush, heapify


def find__index_by_count(heap, count):
    for i in range(len(heap)):
        if heap[i][1] == count:
            return heap[i]


def lift_up(heap, idx, i):
    v = i
    while v > 0 and heap[(v - 1) // 2] > heap[v]:
        heap[(v - 1) // 2], heap[v] = heap[v], heap[(v - 1) // 2]
        idx[heap[(v - 1) // 2][1]], idx[heap[v][1]] = idx[heap[v][1]], idx[heap[(v - 1) // 2][1]]
        v = (v - 1) // 2


def lift_down(heap, idx, i):
    v = i
    l = r = None
    while True:
        l = 2 * v + 1
        r = 2 * v + 2
        if l >= len(heap):
            break
        if l == len(heap) - 1:
            if heap[l] >= heap[v]:
                break
            heap[l], heap[v] = heap[v], heap[l]
            idx[heap[l][1]], idx[heap[v][1]] = heap[heap[v][1]], idx[heap[l][1]]
            v = l
        else:
            min_child_id = r if heap[r] < heap[l] else l
            if heap[v] < heap[min_child_id]:
                break
            heap[v], heap[min_child_id] = heap[min_child_id], heap[v]
            idx[heap[v][1]], idx[heap[min_child_id][1]] = idx[heap[min_child_id]], idx[heap[v][1]]
            v = min_child_id


if __name__ == '__main__':
    heap = []
    n = int(input())
    count = 0
    idx = []

    for i in range(n):
        operation = input()
        if operation[0] == 'A':
            arg = int(operation[4:(len(operation) - 1)])
            heappush(heap, (arg, count))
            count += 1
        elif operation[0] == 'D':
            arg = int(operation[4:(len(operation) - 1)]) - 1
            el = find__index_by_count(heap, arg)
            heap.remove(el)
            heapify(heap)
        else:
            arg = int(operation[5:(len(operation) - 1)])
            print(nsmallest(arg, heap)[0][0])
