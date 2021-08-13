
from project.mammal import Mammal
from unittest import TestCase, main

class MammalTests(TestCase):
    def setUp(self):
        self.mammal = Mammal("Test", "TestType", "rawr")
    
    def test_mammal_init(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("TestType", self.mammal.type)
        self.assertEqual("rawr", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_mammal_make_sound(self):
        self.assertEqual("Test makes rawr", str(self.mammal.make_sound()))

    def test_mammal_get_kingdom(self):
        self.assertEqual("animals", str(self.mammal.get_kingdom()))

    def test_mammal_info(self):
        self.assertEqual("Test is of type TestType", str(self.mammal.info()))


if __name__ == "__main__":
    main()