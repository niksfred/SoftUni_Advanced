class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'

import unittest
class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker("Test", 100, 10)

    def test_worker_is_initialised_correctly(self):
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_worker_energy_increased_after_work(self):
        self.assertEqual(10 ,self.worker.energy)
        self.worker.rest()
        self.assertEqual(11 ,self.worker.energy)
    
    def test_worker_negative_energy_raises(self):
        worker = Worker("Test", 100, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))
    
    def test_worker_work_method_salary_gain(self):
        self.worker.work()
        self.assertEqual(100, self.worker.money)

    def test_worker_work_method_energy(self):
        self.worker.work()
        self.assertEqual(9, self.worker.energy)

    def test_worker_get_info(self):
        result = self.worker.get_info()
        expected_result = f'Test has saved 0 money.'
        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()