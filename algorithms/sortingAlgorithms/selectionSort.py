"""
Selection Sort
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = 1 # assume the first element is the minimum
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j # update the index of the minimum element
        arr[i], arr[min_index] = arr[min_index], arr[i] # swap the minimum element with the first element

if __name__ == '__main__':
    arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
    selectionSort(arr)
    print(arr)