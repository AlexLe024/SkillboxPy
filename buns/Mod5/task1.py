class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None


class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        if self.end is None:
            raise Exception("Стек пуст, нельзя выполнить pop.")
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        new_node = Node(val)
        if self.end is None:
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end = new_node

    def print(self):
        if self.end is None:
            print("Стек пуст.")
            return
        current = self.end
        while current:
            print(current.data, end=" ")
            current = current.pref
        print()

stack = Stack()

while True:
    user_input = input("Введите элемент для добавления в стек (или 'q' для выхода): ")

    if user_input == 'q':
        break

    try:
        value = int(user_input)
        stack.push(value)
        print(f"Добавлен элемент {value} в стек.")
    except ValueError:
        print("Неверный ввод. Введите целое число или 'q' для выхода.")

print("Содержимое стека:")
stack.print()
