# Register Test case

import unittest


class Register(unittest.TestCase):

    def test_registerById(self):
        print("Register by User ID")

    def test_registerByEmail(self):
        print("Register by Email")

    def test_registerbyMobile(self):
        print("Register by Mobile")


if __name__ == "__main__":
    unittest.main()
