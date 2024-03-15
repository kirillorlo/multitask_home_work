import random
import asyncio
import time

arr = [random.randint(1, 100) for _ in range(1000000)]


async def calculate_sum(start, end):
    return sum(arr[start:end])


async def main():
    num_tasks = 4  # Количество задач
    chunk_size = len(arr) // num_tasks  # Размер части массива для каждой задачи

    start_time = time.time()

    # Создание списка корутин
    coroutines = []
    for i in range(num_tasks):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_tasks - 1 else len(arr)
        coro = calculate_sum(start, end)
        coroutines.append(coro)

    # Запуск всех корутин
    results = await asyncio.gather(*coroutines)

    end_time = time.time()

    total_sum = sum(results)

    print(f"Сумма элементов массива: {total_sum}")
    print(f"Затраченное время: {end_time - start_time} секунд(ы)")

# Запуск асинхронной функции
asyncio.run(main())
print(sum(arr))