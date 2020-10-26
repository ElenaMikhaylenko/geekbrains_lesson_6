class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.MassAsphalt = 25
        self.BladeThickness = 5

    def lengthWidth(self):
        return self._length * self._width

    def MassCalculation(self):
        Calculation = self._length * self._width * self.MassAsphalt * self.BladeThickness / 1000
        print(str(int(Calculation)) + " т")


RoadCalculation = Road(20, 5000)
RoadCalculation.MassCalculation()


