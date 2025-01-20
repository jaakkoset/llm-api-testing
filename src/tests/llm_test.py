import unittest
from unittest.mock import Mock
from app import LLM


class TestLLM(unittest.TestCase):
    def setUp(self):
        llm_mock = Mock()
        llm_mock.get_llm_response.return_value = "llm response"
        self.llm = LLM(llm_mock)

    def test_generate_response(self):
        response = self.llm.generate_response(None)
        should_be = "llm response\n\nllm response"
        self.assertEqual(should_be, response)