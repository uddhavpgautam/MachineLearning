import math
class Cylinder:
    height, radius = 0, 0
    def __init__(self, height=1, radius=1):
        (self.height, self.radius) = (height, radius)
    def volume(self):
        volume = math.pi * pow(self.radius, 2) * self.height
        print(round(volume,2))
    def surface_area(self):
        area = 2*math.pi*self.radius*(self.radius+self.height)
        print(round(area,2))
C = Cylinder(2,3)
C.volume()
C.surface_area()
