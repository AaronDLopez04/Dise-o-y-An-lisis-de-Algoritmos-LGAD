import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


sizes = [10, 100, 1000, 10000, 100000]
print("Bubble Sort")
for size in sizes:
    array = [random.randint(1, 10000) for _ in range(size)]
    start_time = time.time()
    bubble_sort(array.copy())
    end_time = time.time()
    print(f"N = {size}, Tiempo = {end_time - start_time:.6f} segundos")
