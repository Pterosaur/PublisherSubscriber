import broker


class subscriber:
    def __init__(self, callback):
        self.__callback = callback

    def callback(self, message):
        self.__callback(message)

    def subscribe(self, broker, topic):
        broker.subscribe(self, topic)