# test_message_processor.py
import unittest
from message_processor import MessageProcessor


class TestMessageProcessor(unittest.TestCase):
    def test_encode_decode_message(self):
        test_data = {"type": "test", "content": "This is a test message"}
        encoded = MessageProcessor.encode_message(test_data)
        decoded = MessageProcessor.decode_message(encoded)
        self.assertEqual(test_data, decoded)


if __name__ == '__main__':
    unittest.main()
