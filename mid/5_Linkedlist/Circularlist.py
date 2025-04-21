class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularSLL:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, prev, item):
        node = Node(item)
        self.size += 1

        if prev:
            node.next = prev.next
            prev.next = node
        else:
            node.next = node  # 자기 자신 가리킴
            self.head = node

    def traverse(self):
        if self.head is None:
            return
        current = self.head
        while True:
            yield current.data
            current = current.next
            if current == self.head:
                break

    def remove(self, prev):
        if self.head is None:
            return

        if self.head.next == self.head:
            self.head = None
            self.size = 0
            return

        if prev is None:
            return

        if prev.next == self.head:
            self.head = self.head.next
        prev.next = prev.next.next
        self.size -= 1
