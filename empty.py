import read_logic
def empty(queue_name):
    read_logic.read_ack(queue_name)
    print(read_logic.is_empty(queue_name))

empty("section1queue")