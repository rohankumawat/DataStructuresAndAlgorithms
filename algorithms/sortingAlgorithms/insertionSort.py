# Insertion Sort Algorithm
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def insertionSort(arr):
    size = len(arr)
    for i in range(1, size):
        for j in range(i, 0, -1):
            # start at i and go back to 0
            # 0 index is exclusive
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else: # if arr[j-1] < arr[j]
                break

if __name__ == '__main__':
    arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
    insertionSort(arr)
    print(arr)