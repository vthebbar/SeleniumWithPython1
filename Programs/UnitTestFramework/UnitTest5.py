# Assertions

import unittest

class Apptest(unittest.TestCase):
    def test_method(self):
        print("Method 1")
        self.assertEqual("First","First", "Strings are not same")

    def test_method2(self):
        print("Method2")
        self.assertNotEqual("First","Second","Strings are not same")


if __name__ == "__main__":
    unittest.main()