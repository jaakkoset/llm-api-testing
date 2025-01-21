import unittest
from useless import Useless


class TestUseless(unittest.TestCase):
    def setUp(self):
        self.useless = Useless()

    def test_multiply_text(self):
        text = self.useless.multiply_text(5, "a")
        should_be = "aaaaa"
        self.assertEqual(should_be, text)

    def test_first_letter(self):
        first_letter = self.useless.first_letter("apple")
        should_be = "a"
        self.assertEqual(should_be, first_letter)

        first_letter = self.useless.first_letter("banana")
        should_be = "b"
        self.assertEqual(should_be, first_letter)

        first_letter = self.useless.first_letter("Apple")
        should_be = "A"
        self.assertEqual(should_be, first_letter)

        first_letter = self.useless.first_letter("Öylätti")
        should_be = "Ö"
        self.assertEqual(should_be, first_letter)
