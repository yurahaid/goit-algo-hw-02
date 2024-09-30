from time import sleep
from queue import Queue

q = Queue()

class Request:
    id = 0
    def __init__(self):
        Request.id += 1
        self.id = Request.id


def generate_request(max_request_count: int):
    req = Request()
    if req.id > max_request_count:
        return

    q.put(req)

def process_request():
    if not q.empty():
        request = q.get()
        print(f'Processing request {request.id}')
    else:
        print('Queue is empty')

def parse_input(user_input: str) -> int:
    return int(user_input)

user_input = input("Enter task count: ")

while True:
    max_request_count = parse_input(user_input)
    generate_request(max_request_count)
    process_request()
    sleep(1)


