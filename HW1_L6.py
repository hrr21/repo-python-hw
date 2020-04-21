from time import sleep


class TrafficLight:
    __color = ["Красный", "Желтый", "Зеленый"]

    def running(self):
        #x = 0
        #while x < 2:
            i = 0
            while i < 3:
                print(f"Светофор переключается: {TrafficLight.__color[i]}")
                if i == 0:
                 sleep(7)
                elif i == 1:
                 sleep(2)
                elif i == 2:
                 sleep(7)
                i += 1
            #x += 1

TrafficLight = TrafficLight()
TrafficLight.running()
