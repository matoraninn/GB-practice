import time


class TrafficLight:
    __color = ['red', 'yellow', 'green']
    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:
                time.sleep(7)
            elif i == 1:
                time.sleep(2)
            elif i == 2:
                time.sleep(6)
            i += 1
tl = TrafficLight()
tl.running()