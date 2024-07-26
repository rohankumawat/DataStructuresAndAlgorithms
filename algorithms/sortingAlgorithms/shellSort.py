# Shell Sort Algorithm
# Time Complexity: O(n log n) - Best Case (Most Gap Sequences)
# Time Complexity: O(n log^2 n) - Best known worst-case gap sequence
# Time Complexity: O(n^2) - Worst Case
# Time Complexity: O(n log^2 n) - Worst case (Best known worst case gap sequence)

def shellSort(arr):
    size = len(arr)
    gap = size // 2

    """
    for i in range(gap, size):
        # start with an anchor element
        anchor = arr[i]
        j = i
        # compare the anchor element with the elements before it
        while j >= gap and arr[j - gap] > anchor:
            arr[j] = arr[j - gap]
            j -= gap
        arr[j] = anchor
    """

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2

if __name__ == '__main__':
    arr = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    shellSort(arr)
    print(arr) # [4, 9, 11, 17, 21, 25, 29, 32, 38]