import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
empty = False


# queue_name = "section1queue"


# while True:
#     method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)
#     if not method_frame:
#         # If there are no more messages, break out of the loop
#         break
#     print("Received message:", body)

def read_ack(queue_name):
    while True:
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)
        if not method_frame:
            break
        print("Received ack message:", body)


def read_no_ack(queue_name):
    global empty
    while True:
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=False)
        if not method_frame:
            empty = False
            break
        print("Received no ack message:", body)


def is_empty(queue_name):
    method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=False)
    return not method_frame


def get_value(queue_name):
    method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=False)
    if "'" not in str(body):
        return str(body).split("'")[0]
    else:
        return ""


def get_all_value(queue_name):
    result = ""
    while True:
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=False)
        if not method_frame:
            break
        if "'" not in str(body):
            result += str(body).split("'")[1]
        print("Received no ack message:", body)
    return result

# def is_empty(queue_name):
#     method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=False)
#     return not method_frame
