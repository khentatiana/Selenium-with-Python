import unittest

class AssertGreaterTest(unittest.TestCase):
    def test(self):
        self.assertGreater(100, 1, "Message if not passed")
        self.assertGreaterEqual(100, 100)
        self.assertLess(1, 100)
        self.assertLessEqual(1, 1)

if __name__ =="__main__":
    unittest.main()