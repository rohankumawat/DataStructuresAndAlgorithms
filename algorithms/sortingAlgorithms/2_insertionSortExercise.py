""" [Insertion Sort Exercise]
Compute the running median of a sequence of numbers.
"""
def running_median(arr):
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        return arr[n//2]
    
def insertionSort(arr):
    for i in range(1, len(arr)):
        #print(running_median(arr[:i]))
        print(i, arr, running_median(arr[:i]))
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break
        # print(running_median(arr[:i]))

if __name__ == '__main__':
    arr = [2, 1, 5, 7, 2, 0, 5]
    insertionSort(arr)
