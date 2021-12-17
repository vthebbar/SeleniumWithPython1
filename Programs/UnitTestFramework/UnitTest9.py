# Assertions - Relation comparison
# assertGreater , assertLess, assertGreaterEqual, assertLessEqual

import unittest

class Apptest(unittest.TestCase):

    def test_method1(self):
        print("Method1")
        self.assertGreater(10,5,"First parameter Not greater than second")

    def test_method2(self):
        print("Method2")
        self.assertLess(1,10,"First parameter is NOT less than second")

    def test_method3(self):
        print("method3")
        self.assertGreaterEqual(10,10,"First parameter NOT >= to second")

    def test_method4(self):
        print("method4")
        self.assertLessEqual(20,20, "First parameter is NOT <= to second")



if __name__ == "__main__":
    unittest.main()