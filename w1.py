import queue
import random
import time

# Створити чергу заявок
request_queue = queue.Queue()

# Генеруємо унікальні номери заявок
request_id = 1

def generate_request():
    global request_id
    request = f"Request {request_id}"
    request_queue.put(request)
    print(f"Generated: {request}")
    request_id += 1

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Processed: {request}")
    else:
        print("Queue is empty. No requests to process.")

# Головний цикл програми
try:
    while True:
        generate_request()
        time.sleep(1)  # Імітуємо час на створення нової заявки
        process_request()
        time.sleep(2)  # Імітуємо час на обробку заявки
except KeyboardInterrupt:
    print("Program stopped.")