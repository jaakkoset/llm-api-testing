import unittest
from unittest.mock import Mock
from app import LLM


class TestLLM(unittest.TestCase):
    def setUp(self):
        self.mock_gemini = Mock()
        self.llm = LLM(self.mock_gemini)

    def test_simulate_customer(self):
        self.mock_gemini.get_response.return_value = "NO"
        response = self.llm.simulate_customers("Mokia")
        should_be = (
            "Customer profiles could not be simulated for the given company Mokia"
        )
        self.assertEqual(should_be, response)

    def test_parse_yes_no_answer(self):
        answer = self.llm.parse_yes_no_answer("\nYES\n")
        self.assertTrue(answer)

        answer = self.llm.parse_yes_no_answer("NO")
        self.assertFalse(answer)

    def test_parse_yes_no_answer_raises_error(self):
        with self.assertRaises(ValueError):
            self.llm.parse_yes_no_answer("invalid")
