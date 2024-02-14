# message_processor.py
import json


class MessageProcessor:
    @staticmethod
    def encode_message(message_data):
        """Encodes a dictionary to a JSON string."""
        return json.dumps(message_data).encode('utf-8')

    @staticmethod
    def decode_message(message_bytes):
        """Decodes a JSON string to a dictionary."""
        return json.loads(message_bytes.decode('utf-8'))
