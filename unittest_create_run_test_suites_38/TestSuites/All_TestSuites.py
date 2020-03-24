import unittest
from unittest_create_run_test_suites_38.Package01.TC_LoginTest import LoginTest
from unittest_create_run_test_suites_38.Package01.TC_SignupTest import SignupTest

from unittest_create_run_test_suites_38.Package02.TC_PaymentReturnsTest import PaymentReturnTest
from unittest_create_run_test_suites_38.Package02.TC_PaymentTest import PaymentTest

# Get all tests from LoginTest, SignupTest, PaymentReturnTest, PaymentTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)

# Creating Test Suites
# Sanity test is includes LoginTest and SignupTest
sanityTestSuite = unittest.TestSuite([tc1, tc2])

# Functional test is includes PaymentReturnTest and PaymentTest
functionalTestSuite = unittest.TestSuite([tc3, tc4])

masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])

unittest.TextTestRunner(verbosity=2).run(sanityTestSuite)






