import random
import multiprocessing
import time

my_list = []
min_number = 1
max_number = 100


def generate_random_number():
    global my_list
    my_list.append(random.randint(min_number, max_number))


# Создание списка процессов
processes = []

start_time = time.time()

# Создание 10 процессов, каждый из которых генерирует случайное число
for _ in range(10):
    p = multiprocessing.Process(target=generate_random_number)
    processes.append(p)
    p.start()

# Ожидание завершения всех процессов
for p in processes:
    p.join()

end_time = time.time()

print(f"Сгенерированный список: {my_list}")
print(f"Сумма сгенерированного списка: {sum(my_list)}")
print(f"Затраченное время: {end_time - start_time} секунд(ы)")