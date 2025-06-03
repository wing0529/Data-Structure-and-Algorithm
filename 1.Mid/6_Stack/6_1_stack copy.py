
# 괄호 유효성 검사 함수
def check_brackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{', '[', '('):     # 여는 괄호는 push
            stack.push(ch)
        if ch in ('}', ']', ')'):     # 닫는 괄호는 짝 검사
            last = stack.pop()

            # 짝이 맞는 경우 continue
            if last == '{' and ch == '}':
                continue
            elif last == '[' and ch == ']':
                continue
            elif last == '(' and ch == ')':
                continue
            else:
                return False          # 짝이 안 맞으면 실패
    if stack.size > 0:                # 남은 여는 괄호가 있으면 실패
        return False
    else:
        return True                   # 전부 짝이 맞으면 성공

# 연결 리스트 노드 정의
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# 연결 리스트 기반 스택 클래스
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):  # top 요소 확인용
        if self.size == 0:
            return None
        return self.top.data



# 검사할 문자열 목록 (괄호 유효성 확인)
sl = ("{(foo)(bar)}[hello](((this)is)a)test",
      "{(foo)(bar)}[hello](((this)is)a test",
      "{(foo)(bar)}[hello](((this)is)a)test(("
      )


for s in sl:
    m = check_brackets(s)
    print("{} : {}".format(s, m))# "문자열1 : 문자열2 {}".format(값1, 값2)
