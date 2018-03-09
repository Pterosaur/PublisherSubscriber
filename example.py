import publisher
import subscriber
import broker

def print_message(message):
    print "publisher : %s \ntopic : %s \npayload : %s \n"%(message.publisher, message.topic, message.payload)

def print_payload(message):
    print "payload : %s \n"%( message.payload)

test_brokyer = broker.broker()

message_subscriber = subscriber.subscriber(print_message)
payload_subscriber = subscriber.subscriber(print_payload)

message_subscriber.subscribe(test_brokyer, "test1")
payload_subscriber.subscribe(test_brokyer, "test1")

test_publisher = publisher.publisher()
test_publisher.add_target(test_brokyer, "test1")
test_publisher.add_target(test_brokyer, "test1")


test_publisher.publish("hello world")
test_publisher.publish("ni hao")


