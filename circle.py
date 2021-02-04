class Circle:
    radius = 0.0

    def __init__(self, new_radius):
        self.radius = new_radius

    def calculate_area(self):
        area = 3.14 * self.radius**2
        print("the area is " + str(self.area))

    def calculate_perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        print("perimeter is " + str(perimeter))