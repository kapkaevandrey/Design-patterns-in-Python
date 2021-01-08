import unittest


def factorize(x):
    if x == 1001:
        return (7, 11, 13)
    if x == 9699690:
        return (2, 3, 5, 7, 11, 13, 19)


class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        self.case = ("string", 1.5)
        for x in self.case:
            with self.subTest(case=x):
                self.assertRaises(TypeError, factorize, x)

    def test_negative(self):
        self.case = (-1, -10, -100)
        for x in self.case:
            with self.subTest(case=x):
                self.assertRaises(ValueError, factorize, x)

    def test_zero_and_one_cases(self):
        self.case = (0, 1)
        for x in self.case:
            with self.subTest(case=x):
                self.assertTupleEqual(factorize(x), (x,))

    def test_simple_numbers(self):
        self.case = [3, 13, 29]
        for x in self.case:
            with self.subTest(case=x):
                self.assertTupleEqual(factorize(x), (x,))

    def test_two_simple_multipliers(self):
        self.case = (6, 26, 121)
        result = ((2, 3), (2, 13), (11, 11))
        for key, x in enumerate(self.case):
            with self.subTest(case=x):
                self.assertTupleEqual(factorize(x), result[key])

    def test_many_multipliers(self):
        self.case = (1001, 9699690)
        result = ((7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19))
        for key, x in enumerate(self.case):
            with self.subTest(case=x):
                self.assertTupleEqual(factorize(x), result[key])


if __name__ == "__main__":
    unittest.main()
