import time
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

sizes = [10, 100, 1000, 10000, 100000]
print("Insertion Sort")
for size in sizes:
    array = [random.randint(1, 10000) for _ in range(size)]
    start_time = time.time()
    insertion_sort(array.copy())
    end_time = time.time()
    print(f"N = {size}, Tiempo = {end_time - start_time:.6f} segundos")
