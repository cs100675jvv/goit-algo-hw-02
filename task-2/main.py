from collections import deque

def is_palindrome(s: str) -> bool:
    # Функція для очищення рядка: видалення пробілів та приведення до нижнього регістру
    def clean_string(s: str) -> str:
        return ''.join(char.lower() for char in s if char.isalnum())

    # Очищаємо вхідний рядок
    cleaned_s = clean_string(s)
    
    # Створюємо двосторонню чергу
    dq = deque(cleaned_s)
    
    # Порівнюємо символи з обох кінців черги
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
            
    return True

# Приклади використання
print(is_palindrome("A man a plan a canal Panama"))  # Повинен повертати True
print(is_palindrome("Was it a car or a cat I saw"))  # Повинен повертати True
print(is_palindrome("No 'x' in Nixon"))              # Повинен повертати True
print(is_palindrome("Hello World"))                  # Повинен повертати False
