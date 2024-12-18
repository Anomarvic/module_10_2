import threading
from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.days = 1
        self.warriors = 100

    def battle(self):
        while self.warriors > 0:
            self.warriors -= self.power
            print(f'{self.name} сражается {self.days} день.., осталось {self.warriors} воинов.')
            self.days += 1
            time.sleep(1)

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.battle()
        print(f'{self.name} одержал победу спустя {(self.days - 1)} дней!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')