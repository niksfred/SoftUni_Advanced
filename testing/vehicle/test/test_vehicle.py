from project.vehicle import Vehicle

from unittest import TestCase, main

class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(25.5, 143.5)

    def test_vehicle_init(self):
        self.assertEqual(25.5, self.vehicle.fuel)
        self.assertEqual(25.5, self.vehicle.capacity)
        self.assertEqual(143.5, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_vehicle_drive_method(self):
        self.vehicle.drive(10)
        self.assertEqual(13.0, self.vehicle.fuel)

    def test_vehicle_drive_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(30)
        self.assertEqual("Not enough fuel", str(ex.exception))
    
    def test_vehicle_refuel_method(self):
        self.vehicle.drive(10)
        self.vehicle.refuel(5)
        self.assertEqual(18.0, self.vehicle.fuel)

    def test_vehicle_refuel_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_vehicle_str_dunder(self):
        expected_result = "The vehicle has 143.5 horse power with 25.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_result, str(self.vehicle.__str__()))

if __name__ == "__main__":
    main()
