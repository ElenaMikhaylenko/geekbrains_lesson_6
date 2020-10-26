class Car:

    #атрибуты

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        self._max_speed = 120

    def go(self):
        print(f"{self.name} is start")

    def stop(self):
        print(f"{self.name} is stop")

    def turn(self, direction):
        print(f"Turn: {direction}")

    def _check_speed(self):
        if self._max_speed < self.speed:
            print("Over speed")

    def show_speed(self):
        print(f"Current speed: {self.speed}")
        self._check_speed()


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._max_speed = 40


class SportCar(Car):

    def _check_speed(self):
        ...


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._max_speed = 60


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

    def _check_speed(self):
        ...


bently = TownCar(50, "green", "bently")
print(bently.speed, bently.color, bently.name, bently.is_police)
bently.turn("forward")
bently.go()
bently.show_speed()
bently.stop()

chevrolet = SportCar(60, "blue", "chevrolet")
print(chevrolet.speed, chevrolet.color, chevrolet.name, chevrolet.is_police)
chevrolet.go()
chevrolet.turn("right")
chevrolet.show_speed()
chevrolet.stop()

mazda = WorkCar(61, "yellow", "mazda")
print(mazda.speed, mazda.color, mazda.name, mazda.is_police)
mazda.show_speed()

nissan = PoliceCar(140, "white", "nissan")
print(nissan.speed, nissan.color, nissan.name, nissan.is_police)
nissan.go()
nissan.stop()
nissan.show_speed()
