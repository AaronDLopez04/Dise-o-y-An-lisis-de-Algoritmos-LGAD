def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) // 2

    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid


def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        pos = binary_search(arr, val, 0, i - 1)
        arr = arr[:pos] + [val] + arr[pos:i] + arr[i + 1:]

    return arr

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Arreglo original:", arr)
    sorted_arr = insertion_sort(arr)
    print("Arreglo ordenado:", sorted_arr)
