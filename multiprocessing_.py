import random
import multiprocessing
import time

arr = [random.randint(1, 100) for _ in range(1000000)]


def calculate_sum(start, end):
    return sum(arr[start:end])


num_processes = 4  # Количество процессов для обработки
chunk_size = len(arr) // num_processes  # Размер части массива для каждого процесса

start_time = time.time()

# Создание списка процессов
processes = []
for i in range(num_processes):
    start = i * chunk_size
    end = (i + 1) * chunk_size if i < num_processes - 1 else len(arr)
    p = multiprocessing.Process(target=calculate_sum, args=(start, end))
    processes.append(p)
    p.start()

# Ожидание завершения всех процессов
for p in processes:
    p.join()

end_time = time.time()

total_sum = sum([p.exitcode for p in processes])

print(f"Сумма элементов массива: {total_sum}")
print(f"Затраченное время: {end_time - start_time} секунд(ы)")
print(sum(arr))