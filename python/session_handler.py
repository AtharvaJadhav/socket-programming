# Extended session_handler.py with metrics

class SessionHandler:
    def __init__(self):
        self.sessions = []
        self.session_metrics = {}

    def add_session(self, client_socket):
        self.sessions.append(client_socket)
        self.session_metrics[client_socket] = {
            'bytes_received': 0, 'bytes_sent': 0}

    def update_metrics_received(self, client_socket, num_bytes):
        if client_socket in self.session_metrics:
            self.session_metrics[client_socket]['bytes_received'] += num_bytes

    def update_metrics_sent(self, client_socket, num_bytes):
        if client_socket in self.session_metrics:
            self.session_metrics[client_socket]['bytes_sent'] += num_bytes

    def remove_session(self, client_socket):
        self.sessions.remove(client_socket)
        del self.session_metrics[client_socket]

    # Additional methods to get metrics or report them can be added here
