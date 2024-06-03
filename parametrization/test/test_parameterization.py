import unittest
from parametrization.core import calculate_volume


class MyTestCase(unittest.TestCase):
    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_volume(-1)

    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            calculate_volume(0)

    def test_wrong_arg_radius(self):
        with self.assertRaises(TypeError):
            calculate_volume("")

        with self.assertRaises(TypeError):
            calculate_volume(None)

        with self.assertRaises(TypeError):
            calculate_volume(False)

    def test_calculate_volume(self):
        self.assertAlmostEqual(calculate_volume(1), 4.18879, places=5)
        self.assertAlmostEqual(calculate_volume(50), 523598.77560, places=5)


if __name__ == '__main__':
    unittest.main()
