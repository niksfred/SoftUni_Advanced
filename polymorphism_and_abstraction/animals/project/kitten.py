from project.cat import Cat

class Kitten(Cat):
    def __init__(self, name, age) -> None:
        super().__init__(name, age, "Female")
    
    def __repr__(self):
        return super().__repr__()

    def make_sound(self):
        return "Meow"
