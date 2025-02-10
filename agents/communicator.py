class Communicator:
    def __init__(self):
        self.logs = []

    def communicate(self, message):
        """Sends mission updates and logs communication."""
        self.logs.append(message)
        print(f"Communicator: Transmitting -> {message}")
