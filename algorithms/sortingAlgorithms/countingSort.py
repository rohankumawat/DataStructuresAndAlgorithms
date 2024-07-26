# Counting Sort
"""
Counting Sort is a sorting algorithm that sorts the elements of an array by 
counting the number of occurrences of each unique element in the array. 
The algorithm is efficient when the range of input data is not significantly 
greater than the number of elements in the array.
"""
# Time Complexity: O(n + k) - where n is the number of elements in the array - k is the max value in the array
# Space Complexity: O(k)

def countingSort(arr):
    n = len(arr)
    maxx = max(arr) # find the maximum value in the array
    counts = [0] * (maxx + 1) # create a list to store the counts of each element

    for x in arr:
        counts[x] += 1
    
    i = 0 # index for the original array
    for c in range(maxx + 1):
        """
        for _ in range(counts[c]):
            arr[i] = c
            i += 1
        """
        while counts[c] > 0:
            arr[i] = c # update the original array
            i += 1 # increment the index
            counts[c] -= 1 # decrement the count

if __name__ == '__main__':
    arr = [4, 2, 2, 8, 3, 3, 1]
    countingSort(arr)