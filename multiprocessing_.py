import random
import multiprocessing
import time

min_numb = 1
max_numb = 10
arr = []

for i in range(1000000):
    arr.append(random.randint(min_numb, max_numb))


def calculate_sum(start, end):
    return sum(arr[start:end])


if __name__ == '__main__':
    num_processes = 4
    chunk_size = len(arr) // num_processes
    start_time = time.time()

    processes = []
    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_processes - 1 else len(arr)
        p = multiprocessing.Process(target=calculate_sum, args=(start, end))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()

    total_sum = sum([p.exitcode for p in processes])

    print(f"Затраченное время: {end_time - start_time} секунд")
