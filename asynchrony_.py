import random
import asyncio
import time

min_numb = 1
max_numb = 10
arr = []

for i in range(1000000):
    arr.append(random.randint(min_numb, max_numb))


async def calculate_sum(start, end):
    return sum(arr[start:end])


async def main():
    num_tasks = 4
    chunk_size = len(arr) // num_tasks

    start_time = time.time()

    coroutines = []
    for i in range(num_tasks):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_tasks - 1 else len(arr)
        coro = calculate_sum(start, end)
        coroutines.append(coro)

    results = await asyncio.gather(*coroutines)

    end_time = time.time()

    total_sum = sum(results)

    print(f"Сумма элементов массива: {total_sum}")
    print(f"Затраченное время: {end_time - start_time} секунд")

asyncio.run(main())
