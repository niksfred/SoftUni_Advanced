from extended_list import IntegerList
from unittest import TestCase, main

class IntegerListTests(TestCase):
    def setUp(self):
        self.int_list = IntegerList(1, 2)

    def test_init(self):
        self.int_list = IntegerList(1, 2, 3.5, "not int")
        self.assertEqual([1, 2], self.int_list._IntegerList__data)
    
    def test_integerlist_add(self):
        self.int_list.add(5)
        self.assertEqual([1, 2, 5], self.int_list._IntegerList__data)

    def test_integerlist_add_not_int(self):
        with self.assertRaises(ValueError) as ex:
            self.int_list.add("not int")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_integerlist_remove_index_method(self):
        self.assertEqual(1, self.int_list.remove_index(0))
        self.assertEqual([2], self.int_list._IntegerList__data)

    def test_integerlist_remove_index_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.remove_index(5)
        self.assertEqual("Index is out of range", str(ex.exception))
    
    def test_integerlist_get_method(self):
        self.assertEqual(1, self.int_list.get(0))

    def test_integerlist_get_method_index_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.get(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_integerlist_insert_method(self):
        self.int_list.insert(1, 3)
        self.assertEqual([1, 3, 2], self.int_list._IntegerList__data)

    def test_integerlist_insert_method_index_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.insert(3, 5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_integerlist_insert_method_el_not_int(self):
        with self.assertRaises(ValueError) as ex:
            self.int_list.insert(1, "not int")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_integerlist_get_biggest(self):
        self.assertEqual(2, self.int_list.get_biggest())

    def test_integerlist_get_index(self):
        self.assertEqual(0, self.int_list.get_index(1))


if __name__ == "__main__":
    main()
