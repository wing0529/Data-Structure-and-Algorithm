from Circularlist import CircularSLL

n, m = map(int, input().split())

circle = CircularSLL()
circle.insert(None, 1)# 1 추가

for i in range(n,1,-1):# n ~ 2까지 1씩 줄이면서 추가
    circle.insert(circle.head,i) #1 다음으로 계속 추가됨 
    # n = 7일때 
    # 1 7 
    # 1 6 7 
    # 1 5 6 7 
    # 1 4 5 6 7 
    # 1 3 4 5 6 7
    # 1 2 3 4 5 6 7

print('<',end='')
prev = circle.head 

while prev.next.data != m: # 제거 대상 노드(prev.next)의 직전 노드(prev)찾기
    # prev.next.data == m일 때 ! 
    prev = prev.next 
    # 이제 prev는 2 = prev.next가 됨

while circle.size > 1: # linked list사이즈가 1개가 될때까지
    print("%d, "% prev.next.data, end='')
    circle.remove(prev) # prev 다음 노드 삭제 : prev =2 였음으로, 3이 삭제됨
    for i in range(m-1): # 계속 반복
        prev = prev.next

print("%d>" % prev.data)
