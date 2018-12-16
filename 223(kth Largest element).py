import math
import random


def partition(arr, start, end):
    pivot = arr[start]
    i = start + 1
    j = end

    while i < j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[start], arr[j] = arr[j], arr[start]
    return j


def find_kth_smallest_element(arr, start, end, k):
    if start < end:
        p = partition(arr, start, end)
        if p == k - 1:
            return arr[p]
        if p > k - 1:
            return find_kth_smallest_element(arr, start, p, k)
        if p < k - 1:
            return find_kth_smallest_element(a, p + 1, end, k)
    return -1


# Function to return sequence built by formula
def get_seq(arr, a, b, c, r, n):
    for i in range(2, n):
        t = a * arr[i - 2] + b * arr[i - 1] + c
        t = t - math.trunc(t / r) * r
        arr.append(round(t))


if __name__ == '__main__':
    n, k = map(int, input().split())
    x_1, x_2 = map(int, input().split())
    a, b, c, r = [int(x) for x in input().split()]
    arr = [x_1, x_2]
    get_seq(arr, a, b, c, r, n)
    print(find_kth_smallest_element(arr, 0, len(arr) - 1, k))
