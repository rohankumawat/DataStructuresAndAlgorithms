# Quick Sort Algorithm
# Time Complexity: O(n log n) - average case
# Worst Case: O(n^2)
# Space Complexity: O(log n) - average case

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1] # last element as the pivot
    L = [x for x in arr[:-1] if x <= pivot] # elements less than the pivot
    R = [x for x in arr[:-1] if x > pivot] # elements greater than the pivot

    L = quickSort(L) # recursively sort the left half
    R = quickSort(R) # recursively sort the right half

    # concatenate the sorted left half, pivot, and sorted right half
    return L + [pivot] + R

if __name__ == '__main__':
    arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
    print(quickSort(arr)) # [-5, -3, -3, 1, 2, 2, 2, 3, 7]