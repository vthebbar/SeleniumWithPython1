# Assertions

import unittest

class Apptest(unittest.TestCase):

    def test_method1(self):
        print("Method1")
        self.assertTrue(1==1,"Not True")

    def test_method2(self):
        print("Method2")
        self.assertFalse(2==1,"Not False")


if __name__ == "__main__":
    unittest.main()