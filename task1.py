from queue import Queue
import random

def create_queue():
    return Queue()

def generate_request(counter):
    return f"Заявка №{counter}"

def add_request_to_queue(q, request):
    q.put(request)
    print(f"Додано: {request}")

def delete_request(q):
    return q.get()

def process_request(q):
    if not q.empty():
        request = delete_request(q)
        print(f"Обробка: {request}")
    else:
        print("Черга порожня")

def main():
    q = create_queue()
    counter = 0

    while True:
        choice = input("1 - нова заявка, 2 - обробити, 0 - вийти: ")
        if choice == "1":
            counter += 1
            add_request_to_queue(q, generate_request(counter))
        elif choice == "2":
            process_request(q)
        elif choice == "0":
            break
        else:
            print("Невідома команда")

main()