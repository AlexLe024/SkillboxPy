class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            raise Exception("Очередь пуста, нельзя выполнить dequeue.")
        value = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def is_empty(self):
        return self.front is None

    def print(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

queue = Queue()

while True:
    try:
        value = input("Введите элемент (или 'q' для завершения): ")
        if value == 'q':
            break
        queue.enqueue(value)
    except Exception as e:
        print(e)

queue.print()

while not queue.is_empty():
    value = queue.dequeue()
    print(f"Извлечено из очереди: {value}")

print(f"Очередь пуста: {queue.is_empty()}")
