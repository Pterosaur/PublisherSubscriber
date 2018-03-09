import broker


class publisher:
    def __init__(self):
        self.__targets = []

    def add_target(self, broker, topic):
        if (broker, topic) not in self.__targets:
            self.__targets.append((broker, topic))
    

    def publish(self, payload):
        for target in self.__targets:
            message = broker.message(target[1], payload, self)
            target[0].publish(message)