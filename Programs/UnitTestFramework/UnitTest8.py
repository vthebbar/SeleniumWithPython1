# Assertions - assertIn and assertNotIn

import unittest

class Apptest(unittest.TestCase):
    def test_method1(self):
        print("Method1")
        list1=[10,20,30,40]
        self.assertIn(40,list1,"Value not found")


    def test_method2(self):
        print("Method2")
        list2=["C","Java","JavaScript","Python"]
        self.assertNotIn("C++",list2,"Value Found")

if __name__ == "__main__":
    unittest.main()