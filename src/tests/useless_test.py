import unittest
from useless import Useless


class TestUseless(unittest.TestCase):
    def setUp(self):
        self.useless = Useless()

    def test_useless(self):
        value = self.useless.useless(21)
        self.assertEqual("BIG", value)

    def test_multiply_text(self):
        text = self.useless.multiply_text(5, "a")
        self.assertEqual("aaaaa", text)

    def test_first_letter(self):
        first_letter = self.useless.first_letter("apple")
        self.assertEqual("a", first_letter)

        first_letter = self.useless.first_letter("banana")
        self.assertEqual("b", first_letter)

        first_letter = self.useless.first_letter("Apple")
        self.assertEqual("A", first_letter)

        first_letter = self.useless.first_letter("Öylätti")
        self.assertEqual("Ö", first_letter)
