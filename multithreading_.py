import random
import concurrent.futures
import time

arr = [random.randint(1, 100) for _ in range(1000000)]

def calculate_sum(chunk):
    return sum(chunk)

num_threads = 4  # Количество потоков для обработки
chunk_size = len(arr) // num_threads  # Размер части массива для каждого потока

start_time = time.time()

# Разбиение массива на части
chunks = [arr[i:i+chunk_size] for i in range(0, len(arr), chunk_size)]

# Создание пула потоков
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Вычисление суммы каждой части массива параллельно
    results = executor.map(calculate_sum, chunks)

# Вычисление общей суммы
total_sum = sum(results)

end_time = time.time()

print(f"Сумма элементов массива: {total_sum}")
print(f"Затраченное время: {end_time - start_time} секунд(ы)")