from util import time_it

@time_it
def linear_search(arr, target):
    for index, value in enumerate(arr): # O(n)
        if value == target: # O(1)
            return index
    return -1

@time_it
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right: # O(log n)
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

@time_it
def binary_search_recursive(arr, target, left, right):
    if left > right: # O(log n)
        return -1 # base case
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

if __name__ == '__main__':
    # numbers = [12, 15, 17, 19, 21, 24, 45, 67]
    # target = 21
    numbers = [i for i in range(1000001)]
    target = 1000000

    print(linear_search(numbers, target))
    print(binary_search(numbers, target))
    print(binary_search_recursive(numbers, target, 0, len(numbers) - 1))