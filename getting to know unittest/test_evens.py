import unittest
from evens import even_number_of_evens  # import function


class TestEvens(unittest.TestCase):

    def test_throw_error_if_value_passed_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)

    def test_value_in_list(self):
        self.assertEqual(even_number_of_evens([]), False)
        self.assertEqual(even_number_of_evens([2, 4]), True)
        self.assertEqual(even_number_of_evens([2]), False)
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)


if __name__ == '__main__':
    unittest.main()
