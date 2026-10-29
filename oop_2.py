class Circle:
    def __init__(self, r):
        self.radius = r

    def get_area(self):
        return 22/7*self.radius**2

    def get_perimeter(self):
        return 22/7*self.radius*2

    def print_details(self):
        print("Radius:", self.radius)
        print("Perimeter:", self.get_perimeter())
        print("Area:", self.get_area())

c1 = Circle(13)
c2= Circle(35)

c1.print_details()
print("Circle 1 Area: ", c1.get_area())

print("Circle 2 Perimeter: ", c2.get_perimeter())