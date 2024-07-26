# Bubble Sort Algorithm
# Time Complexity: O(n^2)
# Space Complexity: O(1) - in place sorting algorithm

# while loop
def bubbleSort(arr):
    n = len(arr) # length of the array
    flag = True # flag to check if the array is already sorted (basically means that we're not done yet)
    while flag: # while the array is not sorted
        flag = False # set the flag to False (we're done)
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                flag = True # if we find a pair of elements that are not sorted, set the flag to True
                arr[i - 1], arr[i] = arr[i], arr[i - 1] # swap the elements
                
# for loop
def bubbleSortFor(arr):
    size = len(arr) # length of the array
    for i in range(size - 1): # iterate through the array
        flag = False
        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                flag = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not flag:
            break

if __name__ == '__main__':
    arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
    bubbleSort(arr)
    print(arr)
    arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
    bubbleSortFor(arr)
    print(arr)