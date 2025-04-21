# 단일 연결 리스트 (Singly Linked List) 전체 구현
# 노드 삽입, 삭제, 순회 가능

#Node 클래스: 연결 리스트의 기본 단위 (데이터 + 다음 노드 주소)
class Node:
    def __init__(self, data=None):
        self.data = data       # 저장할 데이터
        self.next = None       # 다음 노드를 가리키는 포인터


#연결 리스트 클래스 정의
class SinglyLinkedList:
    def __init__(self):
        self.head = None       # 리스트의 첫 번째 노드
        self.size = 0          # 노드 개수

    # 삽입 메서드
    def insert(self, prev, item):
        """
        prev: 삽입할 위치의 이전 노드 (None이면 head 앞 삽입)
        item: 삽입할 데이터
        """
        node = Node(item)
        self.size += 1

        if prev:
            # 중간 삽입: 새 노드 → prev.next 로 연결한 뒤, prev → node로 연결
            # 순서 주의! 먼저 node.next 설정해야 기존 노드를 잃지 않음
            node.next = prev.next
            prev.next = node
        else:
            # 맨 앞 삽입: 새 노드를 head 앞에 삽입
            node.next = self.head
            self.head = node

    # 순회 메서드 (generator로 반환)
    def traverse(self):
        """
        리스트 전체 순회: 하나씩 데이터 반환 (yield = 반복자 생성)
        """
        current = self.head
        while current:
            yield current.data  # return과 달리 함수가 중단되지 않고 유지됨
            current = current.next

    # 삭제 메서드
    def remove(self, prev):
        """
        prev: 삭제할 노드의 이전 노드 (None이면 head를 삭제)
        """
        self.size -= 1

        if prev:
            # 중간 삭제: prev → (삭제할 노드 건너뛰기) → prev.next.next
            prev.next = prev.next.next
        else:
            # 맨 앞 삭제: head → head.next
            self.head = self.head.next
