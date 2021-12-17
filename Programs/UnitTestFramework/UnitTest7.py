# Assertions - assertIsNone and assertIsNotNone

import unittest

class Apptest(unittest.TestCase):
    def test_method1(self):
        data1=None
        print("method1", data1)
        self.assertIsNone(data1,"Not None value")

    def test_method2(self):
        data2=10
        print("Method2",data2)
        self.assertIsNotNone(data2, "None value")

if __name__ == "__main__":
    unittest.main()