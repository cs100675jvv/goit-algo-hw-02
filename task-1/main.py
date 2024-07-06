import queue
import random
import time

# Створити чергу заявок
request_queue = queue.Queue()

# Унікальний ідентифікатор для заявок
request_id = 0

def generate_request():
    global request_id
    request_id += 1
    request = f"Заявка {request_id}"
    request_queue.put(request)
    print(f"Згенеровано {request}")

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Обробка {request}")
        time.sleep(1)  # Імітація часу на обробку заявки
        print(f"{request} оброблено")
    else:
        print("Черга пуста, немає заявок для обробки")

def main():
    while True:
        user_input = input("Введіть 'g' для генерації заявки, 'p' для обробки заявки, 'q' для виходу: ").strip().lower()
        
        if user_input == 'g':
            generate_request()
        elif user_input == 'p':
            process_request()
        elif user_input == 'q':
            print("Вихід з програми")
            break
        else:
            print("Невідома команда, спробуйте ще раз")

if __name__ == "__main__":
    main()
