class Node:
    def __init__(self, data=None):
        self.data = data        # 노드에 저장할 데이터
        self.next = None        # 다음 노드 포인터 (순환 연결용)


class CircularSLL:
    def __init__(self):
        self.head = None        # 첫 노드(시작점)
        self.size = 0           # 노드 개수

    def insert(self, prev, item):
        node = Node(item)
        self.size += 1

        if prev:
            # 새 노드를 prev 다음에 삽입 (prev → node → prev.next)
            node.next = prev.next
            prev.next = node
        else:
            # 리스트가 비어있을 경우: 첫 노드로 삽입
            node.next = node       # 자기 자신을 가리킴 (순환 구조 유지)
            self.head = node       # head로 지정

    def traverse(self):
        current = self.head
        while True:
            yield current.data     # 현재 노드 데이터 반환
            if current.next == self.head:
                break              # 한 바퀴 돌면 종료
            else:
                current = current.next

    def remove(self, prev):
        # prev.next 노드를 삭제한다
        self.size -= 1

        if prev.next != self.head:
            prev.next = prev.next.next  # 일반 노드 삭제
        else:
            if prev != self.head:
                self.head = self.head.next      # head 삭제 → 다음 노드를 head로
                prev.next = self.head
            else:
                self.head = None               # 마지막 하나 삭제
