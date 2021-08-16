from project.pet_shop import PetShop

from unittest import TestCase, main

class PetShopTests(TestCase):
    def setUp(self):
        self.p = PetShop("Test")

    def test_petshop_init(self):
        p = PetShop("Test")
        self.assertEqual("Test", p.name)
        self.assertEqual([], p.pets)
        self.assertEqual({}, p.food)

    def test_petshop_add_food_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.p.add_food("food",-5)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_petshop_add_food_not_present(self):
        self.assertEqual("Successfully added 5.00 grams of testfood.", self.p.add_food("testfood", 5))
        self.assertEqual({"testfood": 5},self.p.food)


    def test_petshop_add_food_present(self):
        self.p.add_food("testfood", 5)
        self.assertEqual("Successfully added 5.00 grams of testfood.", self.p.add_food("testfood", 5))
        self.assertEqual({"testfood": 10},self.p.food)

    def test_petshop_add_pet_raises(self):
        self.p.add_pet("Test")
        with self.assertRaises(Exception) as ex:
            self.p.add_pet("Test")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_petshop_add_pet(self):
        self.assertEqual("Successfully added Test.",self.p.add_pet("Test")) 
        self.assertEqual(["Test"], self.p.pets)

    def test_petshop_feed_pet_raises(self):
        self.p.add_food("testfood", 5)
        with self.assertRaises(Exception) as ex:
            self.p.feed_pet("testfood", "Test")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_petshop_feed_pet_no_food_name(self):
        self.p.add_pet("Test")
        #self.p.feed_pet("testfood", "Test")
        self.assertEqual('You do not have testfood', self.p.feed_pet("testfood", "Test"))

    def test_petshop_feed_pet_not_enough_food(self):
        self.p.add_pet("Test")
        self.p.add_food("testfood", 5)
        self.assertEqual("Adding food...", self.p.feed_pet("testfood", "Test"))
        self.assertEqual({"testfood":1005.00}, self.p.food)

    def test_petshop_feed_pet(self):
        self.p.add_pet("Test")
        self.p.add_food("testfood", 500)
        self.assertEqual("Test was successfully fed", self.p.feed_pet("testfood", "Test"))
        self.assertEqual({"testfood": 400.00}, self.p.food)

    def test_petshop_repr(self):
        self.p.add_pet("Test")
        expected_result = "Shop Test:\nPets: Test"
        self.assertEqual(expected_result, repr(self.p))

if __name__ == "__main__":
    main()