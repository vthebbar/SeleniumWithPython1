# To illustrate use of unittest framework methods

import unittest

def setUpModule():
        print("Before module")

def tearDownModule():
    print("After module")


class AppTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("Before method- Login Function code")

    @classmethod
    def tearDown(self):
        print("After method-Log Out Function Code")

    @classmethod
    def setUpClass(cls):
        print("Before All methods- Launch Application/browser code")

    @classmethod
    def tearDownClass(cls):
        print("After all methods-Close application/browser code")

    def test_register(self):
        print("Registration function")

    def test_search(self):
        print("Search Function")

    def test_display(self):
        print("Display function")

if __name__ == "__main__":
    unittest.main()

