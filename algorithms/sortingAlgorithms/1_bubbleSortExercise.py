def bubbleSort(arr, key=None):
    size = len(arr)
    for i in range(size - 1):
        flag = False
        for j in range(size - 1 - i):
            if arr[j][key] > arr[j + 1][key]:
                flag = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not flag:
            break

if __name__ == '__main__':
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    bubbleSort(elements, key='transaction_amount')
    print(elements)

    bubbleSort(elements, key='name')
    print(elements)