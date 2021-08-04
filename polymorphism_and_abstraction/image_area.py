class ImageArea:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __eq__(self, o: object) -> bool:
        return self.get_area() == o.get_area()

    def __ne__(self, o: object) -> bool:
        return self.get_area() != o.get_area()

    def __gt__(self, o: object) -> bool:
        return self.get_area() > o.get_area()

    def __ge__(self, o: object) -> bool:
        return self.get_area() >= o.get_area()
    
    def __lt__(self, o: object) -> bool:
        return self.get_area() < o.get_area()
    
    def __le__(self, o: object) -> bool:
        return self.get_area() <= o.get_area()



    

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)
