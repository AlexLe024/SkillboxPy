class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, index):
        if index < 0:
            return None

        current = self.head
        current_index = 0

        while current:
            if current_index == index:
                return current.data
            current = current.next
            current_index += 1

        return None

    def remove(self, index):
        if index < 0:
            return

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        current_index = 0

        while current and current_index < index - 1:
            current = current.next
            current_index += 1

        if current and current.next:
            current.next = current.next.next

    def insert(self, n, val):
        if n <= 0:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        current_index = 0

        while current and current_index < n - 1:
            current = current.next
            current_index += 1

        if current:
            new_node = Node(val)
            new_node.next = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

my_list = LinkedList()

my_list.push(1)
my_list.push(2)
my_list.push(3)
my_list.push(4)

my_list.display()

my_list.insert(2, 5)

my_list.display()

my_list.remove(1)

my_list.display()
