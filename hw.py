class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def insert(self, data, position):
        new_node = Node(data)

        if position <= 0:
            print("Invalid position! Must be >= 1.")
            return

        if position == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        temp = self.head
        i = 1
        while temp and i < position - 1:
            temp = temp.next
            i += 1

        if temp is None:
            print(f"Position {position} is out of range.")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

dll = DoublyLL()

n = int(input("Enter the number of nodes to insert: "))
for _ in range(n):
    data = int(input("Enter data: "))
    position = int(input("Enter position to insert the node: "))
    dll.insert(data, position)

print("\nFinal Doubly Linked List:")
dll.display()
