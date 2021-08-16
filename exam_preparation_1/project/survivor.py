class Survivor:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.health: int = 100
        self.needs: int = 100

    @property
    def needs_sustenance(self):
        return self.needs < 100
    
    @property
    def needs_healing(self):
        return self.health < 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            raise ValueError("Name not valid!")
        self.__name = new_name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError("Age not valid!")
        self.__age = new_age

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new_health):
        if new_health < 0:
            raise ValueError("Health not valid!")
        if new_health > 100:
            self.__health = 100
        else:
            self.__health = new_health
    
    @property
    def needs(self):
        return self.__needs

    @needs.setter
    def needs(self, new_needs):
        if new_needs < 0:
            raise ValueError("Needs not valid!")
        if new_needs > 100:
            self.__needs = 100
        else:
            self.__needs = new_needs
