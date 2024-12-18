import time
import threading
from time import sleep

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)


    print(f'Завершилась запись в файл {file_name}')

start_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time()
print(f'Время выполнения функций: {end_time - start_time}')


def write_words_th(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)

    print(f'Завершилась запись в файл {file_name}')

start_time_threads = time.time()

# Поскольку не хочется перечислять каждый раз, делаю список из кортежей аргументов
thread_callList = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
    ]

# Для каждого кортежа из списка аргументов для функции
for call in thread_callList:
    # создать новый поток с текущим кортежем аргументов
    thread = threading.Thread(target=write_words_th, args=call)
    # запустить этот поток
    thread.start()
    # Если так как ниже, то многопоточность руинится, т.к. каждый поток встаёт в строгую очередь:
    #thread.join()

# Получаем список всех запущенных потоков
threads_running = threading.enumerate()

# Поскольку первым в списке идёт main поток, берём начиная со второго (индекс 1) и до конца списка
for i in range(1, len(threads_running)):
    # конкретно этот поток джойним
    # как я понимаю, джойнить - ждать его завершения
    # то есть каждый запущенный поток, подождать
    threads_running[i].join()

end_time_threads = time.time()
print(f'Время выполнения функций: {end_time_threads - start_time_threads} ')
