from car_manager import Car

from unittest import TestCase, main

class TestCarManager(TestCase):
    def setUp(self):
        self.car = Car("BMW", "3-series", 14, 60)
        

    def test_init(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("3-series", self.car.model)
        self.assertEqual(14, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_make_setter(self):
        self.car.make = "Audi"
        self.assertEqual("Audi", self.car.make)

    def test_car_make_setter_blank_str(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_car_model_setter(self):
        self.car.model = "A3"
        self.assertEqual("A3", self.car.model)

    def test_car_model_setter_blank_str(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_car_fuel_consumption_setter(self):
        self.car.fuel_consumption = 5
        self.assertEqual(5, self.car.fuel_consumption)

    def test_car_negative_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -5
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))
    
    def test_car_fuel_capacity_setter(self):
        self.car.fuel_capacity = 5
        self.assertEqual(5, self.car.fuel_capacity)

    def test_car_negative_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -5
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_car_fuel_amount_setter(self):
        self.car.fuel_amount = 5
        self.assertEqual(5, self.car.fuel_amount)

    def test_car_negative_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -5
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_car_refuel_method(self):
        self.car.refuel(5)
        self.assertEqual(5, self.car.fuel_amount)

    def test_car_refuel_negative_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-5)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_car_drive(self):
        self.car.fuel_amount = 50
        self.car.drive(100)
        self.assertEqual(36, self.car.fuel_amount)

    def test_car_drive_without_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

if __name__ == "__main__":
    main()
