from collections import deque

def is_palindrome(text):
    text = text.replace(" ", "").lower()
    char_deque = deque(text)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True

def main():
    print("Перевірка на паліндром")
    print("Введіть 'exit' для виходу.")

    while True:
        text = input("Введіть рядок: ")
        if text == "exit":
            break
        result = is_palindrome(text)
        print(f"Результат: {result}")

if __name__ == "__main__":
    main()