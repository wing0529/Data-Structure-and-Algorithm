class Node:
    def __init__(self, key=None):
        self.key = key          # 실제 데이터
        self.prev = None        # 이전 노드
        self.next = None        # 다음 노드


class DoublyLinkedlist:
    def __init__(self):
        self.head = None        # 리스트의 첫 번째 노드 (L.head)
        self.size = 0

    def insert(self, prev, key): # prev : 삽입할 위치의 이전 노드 (None이면 맨 앞) key :삽입할 값 (노드의 key 필드)
        node = Node(key)
        self.size += 1

        if prev:
            node.next = prev.next      # 새 노드가 prev의 다음 노드를 가리킴
            node.prev = prev           # 새 노드는 prev를 가리킴
            prev.next = node           # prev는 새 노드를 가리킴

            if node.next:              # 다음 노드가 존재하면
                node.next.prev = node  # 다음 노드의 prev를 새 노드로 연결
        else:
            # 맨 앞(head) 삽입
            node.next = self.head
            if self.head:
                self.head.prev = node
            self.head = node

    def delete(self, node):# node: 삭제할 노드
        self.size -= 1

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev

    def traverse_forward(self):#  정방향 순회: head → tail
        current = self.head
        while current:
            yield current.key
            current = current.next

    def traverse_backward(self): # 역방향 순회: tail → head
        current = self.head
        if not current:
            return
        while current.next:
            current = current.next  # tail로 이동

        while current:
            yield current.key
            current = current.prev

