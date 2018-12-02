import math

# Function to return k'th smallest
# element in a given array
def kthSmallest(arr, n, k):
    # Sort the given array
    arr.sort()

    # Return k'th element in the
    # sorted array
    return arr[k - 1]

# Function to return sequence built by formula
def getSeq(arr, a, b, c, r, n):
    for i in range(2, n):
        t = a * arr[i - 2] + b * arr[i - 1] + c
        t = t - math.trunc(t / r) * r
        arr.append(round(t))

# Driver code
if __name__ == '__main__':
    n, k = map(int, input().split())
    x_1, x_2 = map(int, input().split())
    a, b, c, r = [int(x) for x in input().split()]
    arr = [x_1, x_2]
    getSeq(arr, a, b, c, r, n)
    l = len(arr)
    print(kthSmallest(arr, l, k))
