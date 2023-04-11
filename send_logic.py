import pika

def declare_queue(queue_name):
    with pika.BlockingConnection(pika.ConnectionParameters("localhost")) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=queue_name)


def send(queue_name, msg):
    with pika.BlockingConnection(pika.ConnectionParameters("localhost")) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=queue_name)
        # updated_text = input("Enter the updated text for section 1: ")
        channel.basic_publish(
            exchange="", routing_key=queue_name, body=msg)
