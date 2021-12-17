# Login Test case

import unittest


class Login(unittest.TestCase):

    def test_loginById(self):
        print("Login by User ID")

    def test_loginByEmail(self):
        print("Login by Email")

    def test_loginbyMobile(self):
        print("Login by Mobile")


if __name__ == "__main__":
    unittest.main()
