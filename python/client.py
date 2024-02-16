import socket


class Client:
    def __init__(self, server_host='127.0.0.1', server_port=65432):
        self.server_host = server_host
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        self.client_socket.connect((self.server_host, self.server_port))
        print(f"Connected to server at {self.server_host}:{self.server_port}")

    def send_message(self, message):
        self.client_socket.sendall((message + "\n").encode('utf-8'))

    def receive_response(self):
        response_bytes = self.client_socket.recv(1024)
        response = response_bytes.decode('utf-8')  # Decode bytes to string
        print("Server response:", response)

    def close_connection(self):
        self.client_socket.close()


if __name__ == "__main__":
    client = Client()
    client.connect_to_server()

    try:
        while True:
            message = input("Enter message (type 'quit' to exit): ")
            if message == 'quit':
                break
            client.send_message(message)
            client.receive_response()
    finally:
        client.close_connection()
