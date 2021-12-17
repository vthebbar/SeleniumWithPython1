# Payment Test case

import unittest

class Payments(unittest.TestCase):

    def test_paybyCard(self):
        print("Payment by card")

    def test_paybyNetBank(self):
        print("Payment by Net banking")

if __name__ == "__main__":
    unittest.main()