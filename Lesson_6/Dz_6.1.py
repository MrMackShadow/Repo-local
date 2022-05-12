from time import sleep
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:

            print(f'{TrafficLight.__color[i]}', flush=False)

            if i == 0:
                sleep(1)
            elif i == 1:
                sleep(1)
            elif i == 2:
                sleep(1)

            i += 1

t = TrafficLight()
t.running()
