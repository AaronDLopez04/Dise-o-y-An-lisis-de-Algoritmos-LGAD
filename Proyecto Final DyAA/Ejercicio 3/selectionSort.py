import time
import random

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

sizes = [10, 100, 1000, 10000, 100000]
print("Selection Sort")
for size in sizes:
    array = [random.randint(1, 10000) for _ in range(size)]
    start_time = time.time()
    selection_sort(array.copy())
    end_time = time.time()
    print(f"N = {size}, Tiempo = {end_time - start_time:.6f} segundos")
