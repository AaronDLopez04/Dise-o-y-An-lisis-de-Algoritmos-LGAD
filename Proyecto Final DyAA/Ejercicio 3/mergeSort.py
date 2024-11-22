import time
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

sizes = [10, 100, 1000, 10000, 100000]
print("Merge Sort")
for size in sizes:
    array = [random.randint(1, 10000) for _ in range(size)]
    start_time = time.time()
    merge_sort(array.copy())
    end_time = time.time()
    print(f"N = {size}, Tiempo = {end_time - start_time:.6f} segundos")
