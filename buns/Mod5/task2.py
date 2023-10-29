class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def pop(self):
        if self.start is None:
            return None
        val = self.start.data
        self.start = self.start.nref
        if self.start is not None:
            self.start.pref = None
        return val

    def push(self, val):
        new_node = Node(val)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def insert(self, n, val):
        new_node = Node(val)
        current = self.start
        for _ in range(n - 1):
            if current is None:
                return
            current = current.nref
        if current is None:
            return
        new_node.pref = current
        new_node.nref = current.nref
        if current.nref is not None:
            current.nref.pref = new_node
        current.nref = new_node

    def print(self):
        current = self.start
        while current is not None:
            print(current.data, end=" ")
            current = current.nref
        print()

q = Queue()

while True:
    print("1. Добавить элемент")
    print("2. Извлечь элемент")
    print("3. Вставить элемент")
    print("4. Вывести очередь")
    print("5. Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        val = int(input("Введите элемент для добавления: "))
        q.push(val)
    elif choice == "2":
        val = q.pop()
        if val is not None:
            print(f"Извлечен элемент: {val}")
        else:
            print("Очередь пуста.")
    elif choice == "3":
        n = int(input("Введите позицию для вставки: "))
        val = int(input("Введите элемент для вставки: "))
        q.insert(n, val)
    elif choice == "4":
        q.print()
    elif choice == "5":
        break
