from time import sleep


class TrafficLight:
    #атрибуты класса
    __color = ["Red", "Yellow", "Green"]

    #метод класса
    def running(self):
        sleep(7)
        print(TrafficLight.__color[0])
        sleep(2)
        print(TrafficLight.__color[1])
        sleep(3)
        print(TrafficLight.__color[2])


traffic_light = TrafficLight()
traffic_light.running()
