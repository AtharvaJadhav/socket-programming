# server.py
from session_handler import SessionHandler
import threading
import socket
from message_processor import MessageProcessor
import sys
import os

# Add the directory containing this script to the Python path
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.append(script_dir)


class Server:
    def __init__(self, host='127.0.0.1', port=65432):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(
            socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.session_handler = SessionHandler()

    def start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Server listening on {self.host}:{self.port}")
        try:
            while True:
                client_socket, addr = self.server_socket.accept()
                print(f"Connection established from {addr}")
                client_thread = threading.Thread(
                    target=self.handle_client, args=(client_socket,))
                client_thread.start()
        except KeyboardInterrupt:
            print("Server is shutting down.")
        finally:
            self.server_socket.close()

    def handle_client(self, client_socket):
        self.session_handler.add_session(client_socket)
        try:
            while True:
                message_bytes = client_socket.recv(1024)
                if message_bytes:
                    message = MessageProcessor.decode_message(message_bytes)
                    print(f"Received message: {message}")
                    # Here, you can add logic to respond to messages
                    response_data = {"response": "Message received"}
                    response_bytes = MessageProcessor.encode_message(
                        response_data)
                    client_socket.sendall(response_bytes)
                else:
                    break
        finally:
            self.session_handler.remove_session(client_socket)
            client_socket.close()


if __name__ == "__main__":
    server = Server()
    server.start_server()
