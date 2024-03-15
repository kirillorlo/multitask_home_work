
import random
import threading
import time

my_list = []
min_number = 1
max_number = 100


def generate_random_number():
    global my_list
    my_list.append(random.randint(min_number, max_number))


# Создание списка потоков
threads = []

start_time = time.time()

# Создание 100 потоков, каждый из которых генерирует случайное число
for _ in range(100):
    t = threading.Thread(target=generate_random_number)
    threads.append(t)
    t.start()

# Ожидание завершения всех потоков
for t in threads:
    t.join()

end_time = time.time()

# print(f"Сгенерированный список: {my_list}")
# print(f"Сумма сгенерированного списка: {sum(my_list)}")
print(f"Затраченное время: {end_time - start_time} секунд(ы)")
