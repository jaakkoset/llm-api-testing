import unittest
from useless import Useless


class TestUseless(unittest.TestCase):
    def setUp(self):
        self.useless = Useless()

    def test_multiply_text(self):
        text = self.useless.multiply_text(5, "a")
        should_be = "aaaaa"
        self.assertEqual(should_be, text)
