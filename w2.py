from collections import deque

def is_palindrome(s):
    # Приведемо рядок до нижнього регістру та видалимо пробіли
    s = ''.join(filter(str.isalnum, s)).lower()
    char_deque = deque(s)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Приклади використання
print(is_palindrome("Madam i'm Adam"))                # True
print(is_palindrome("Level"))                         # True
print(is_palindrome("Oksana"))                        # False