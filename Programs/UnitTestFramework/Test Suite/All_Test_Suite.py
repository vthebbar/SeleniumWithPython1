# Test suite using python unittest framework

import unittest
from Programs.UnitTestFramework.Package1.TC_Login import Login
from Programs.UnitTestFramework.Package1.TC_Register import Register
from Programs.UnitTestFramework.Package2.TC_Payment import Payments
from Programs.UnitTestFramework.Package2.TC_UpdateDetails import Update

tc1 = unittest.TestLoader().loadTestsFromTestCase(Login)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Register)
tc3 = unittest.TestLoader().loadTestsFromTestCase(Payments)
tc4 = unittest.TestLoader().loadTestsFromTestCase(Update)

SanityTestSuite = unittest.TestSuite([tc1, tc2])
FunctionalTestSuite = unittest.TestSuite([tc3, tc4])
MasterTestSuite = unittest.TestSuite([tc1,tc2, tc3, tc4])   # Combination of all test cases

#unittest.TestSuite.addTest(SanityTestSuite, tc4)
#unittest.TextTestRunner().run(SanityTestSuite)
#unittest.TextTestRunner().run(FunctionalTestSuite)

unittest.TextTestRunner().run(MasterTestSuite)