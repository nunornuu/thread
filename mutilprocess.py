from threading import Thread
from time import sleep


count = 0


class Producer(Thread):
    def run(self) -> None:
        global count
        op = True
        while op:
            if count < 50:
                count += 1
                print(f'----{count}')
            else:
                sleep(3)
                # count = count - 40
                op = bool(count < 50)


class Consumer(Thread):
    money = 100
    price = 5

    def run(self) -> None:
        global count
        while self.money:
            if bool(count):
                count -= 1
                self.money -= self.price
                print(f'${self.money}')
            else:
                sleep(3)


p1 = Producer()
p2 = Producer()
p3 = Producer()

p1.start()
p2.start()
p3.start()

c1 = Consumer()
c2 = Consumer()
c3 = Consumer()
c4 = Consumer()
c5 = Consumer()
c6 = Consumer()

c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()
