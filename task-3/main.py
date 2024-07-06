def is_balanced(s: str) -> str:
    # Визначаємо пари відкриваючих і закриваючих символів
    matching_brackets = {')': '(', ']': '[', '}': '{'}
    open_brackets = matching_brackets.values()
    
    # Ініціалізуємо стек
    stack = []
    
    # Проходимо по кожному символу в рядку
    for char in s:
        if char in open_brackets:
            # Якщо символ є відкриваючим, додаємо його до стеку
            stack.append(char)
        elif char in matching_brackets:
            # Якщо символ є закриваючим
            if not stack or stack.pop() != matching_brackets[char]:
                # Якщо стек порожній або верхній елемент стека не відповідає закриваючому символу
                return "Несиметрично"
    
    # Після проходження всіх символів, перевіряємо чи стек порожній
    return "Симетрично" if not stack else "Несиметрично"

# Приклади використання
print(is_balanced("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Повинен повернути "Симетрично"
print(is_balanced("( 23 ( 2 - 3);"))             # Повинен повернути "Несиметрично"
print(is_balanced("( 11 }"))                     # Повинен повернути "Несиметрично"
