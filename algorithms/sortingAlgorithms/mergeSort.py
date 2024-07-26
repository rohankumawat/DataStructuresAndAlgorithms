# Merge Sort Algorithm
# Time Complexity: O(n log n)
# Space Complexity: O(n)

def mergeSort(arr):
    n = len(arr)

    if n == 1:
        return arr
    
    m = len(arr) // 2 # middle index
    left = arr[:m] # left half
    right = arr[m:] # right half

    left = mergeSort(left) # recursively sort the left half
    right = mergeSort(right) # recursively sort the right half
    l, r = 0, 0 # left and right pointers
    l_len, r_len = len(left), len(right) # left and right lengths

     
    sorted_arr = [0] * n # create a new array to store the sorted elements
    i = 0

    while l < l_len and r < r_len:
        if left[l] < right[r]:
            sorted_arr[i] = left[l]
            l += 1
        else:
            sorted_arr[i] = right[r]
            r += 1
        i += 1 # increment the index of the sorted array

    # anything left in the left array
    while l < l_len:
        sorted_arr[i] = left[l]
        l += 1
        i += 1
    
    # anything left in the right array
    while r < r_len:
        sorted_arr[i] = right[r]
        r += 1
        i += 1
    
    return sorted_arr

if __name__ == '__main__':
    arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
    print(mergeSort(arr)) # [-5, -3, -3, 1, 2, 2, 2, 3, 7]