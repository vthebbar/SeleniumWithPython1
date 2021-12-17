# Skip methods - 3 types

import unittest

class AppTest(unittest.TestCase):

    @unittest.SkipTest
    def test_method1(self):
        print("method 1")

    @unittest.skip("Method not ready")
    def test_method2(self):
        print("Method 2")

    @unittest.skipIf(False==False,"Skipped due condition is ture")
    def test_method3(self):
        print("Method 3")

    def test_method4(self):
        print("Method 4")

    def test_method5(self):
        print("Method 5")


if __name__ == "__main__":
    unittest.main()
