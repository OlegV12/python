
from itertools import cycle
from time import sleep


class TrafficLight:
    __color = ["red", "yellow", "green", "yellow"]

    def running(self):
        for el in cycle(TrafficLight.__color):
            print(el)
            if el == "red":
                sleep(7)
            elif el == "yellow":
                sleep(2)
            else:
                sleep(4)


a = TrafficLight()
a.running()

