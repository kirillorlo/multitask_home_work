import random
import concurrent.futures
import time

min_numb = 1
max_numb = 10
arr = []

for i in range(1000000):
    arr.append(random.randint(min_numb, max_numb))


def calculate_sum(chunk):
    return sum(chunk)


num_threads = 4
chunk_size = len(arr) // num_threads

start_time = time.time()

chunks = [arr[i:i+chunk_size] for i in range(0, len(arr), chunk_size)]

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(calculate_sum, chunks)

total_sum = sum(results)

end_time = time.time()

print(f"Затраченное время: {end_time - start_time} секунд")
