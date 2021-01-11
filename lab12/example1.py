import math
class Cylinder:
  def __init__(self, radius, height):
    self.radius = radius
    self.height = height
  def get_radius(self):
    return self.radius
  def get_height(self):
    return self.height
  def set_radius(self,radius):
    if radius > 0:
      self.radius = radius
    print("It cannot be negative number.")
  def set_height(self,height):
    if height > 0:
      self.height = height
    print("It cannot be negative number.")
  def base_area(self):
    return math.pi * (self.radius**2)
  def surface_area(self):
    return 2 * math.pi * self.radius * self.height
  def calculate_area(self):
    return 2 * self.base_area() + self.surface_area()
  def volume(self):
    return self.base_area() * self.height
cylinder1 = Cylinder(3,5)
print(cylinder1.calculate_area())
print(cylinder1.volume())