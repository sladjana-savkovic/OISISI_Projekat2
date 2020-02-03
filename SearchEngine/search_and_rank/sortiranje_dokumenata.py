
def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high].rank #pivot

    for j in range(low, high):

        if arr[j].rank >= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)