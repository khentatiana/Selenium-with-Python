import unittest

class Assert_In(unittest.TestCase):
    def test(self):
        list = {"python", "c++", "ryby", "java"}
        self.assertNotIn("go", list)
