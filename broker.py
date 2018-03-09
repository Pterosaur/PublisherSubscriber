import copy



class message:
    def __init__(self, topic, payload, publisher):
        self.topic = topic
        self.payload = payload
        self.publisher = publisher
        pass


class broker:
    def __init__(self):
        self.__topics = {}
        pass
    
    def subscribe(self, subscriber, topic):
        if topic not in  self.__topics.keys():
            self.__topics[topic] = []
        if subscriber not in self.__topics[topic]:
            self.__topics[topic].append(subscriber)
    
    def publish(self, message):
        if message.topic not in self.__topics.keys():
            return
        for subscribe in self.__topics[message.topic]:
            message = copy.deepcopy(message)
            subscribe.callback(message)
        