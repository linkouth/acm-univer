# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    # Driver code to test above


# Returns index of x in arr if present, else -1
def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

            # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1

if __name__ == '__main__':
    # n = int(input())
    # a = [int(x) for x in input().split()]
    # m = int(input())
    # b = [int(x) for x in input().split()]
    # k = int(input())
    # c = [int(x) for x in input().split()]
    n = 4; m = 2; k = 6
    a = [-2, 3, 1, 17]
    b = [10, 100]
    c = [13, 117, 28, 98, 111, 1]
    quickSort(a, 0, n - 1)
    quickSort(b, 0, m - 1)
    for i in range(k):
        for j in range(n):
            if binarySearch(b, 0, m - 1, c[i] - a[j]) != -1:
                print('YES')
                break
            elif (j == n - 1) and (binarySearch(b, 0, m - 1, c[i] - a[j]) == -1):
                print('NO')
