import unittest


class PaymentTest(unittest.TestCase):
    def test_paymentInDollars(self):
        print("\nThis is payment in dollar test")
        self.assertTrue(True)

    def test_paymentInEuros(self):
        print("\nThis is payment in euros")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()