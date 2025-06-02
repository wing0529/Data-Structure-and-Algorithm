from collections import deque
import sys
input = sys.stdin.readline

# 입력
n = int(input())            # 컴퓨터 수
m = int(input())            # 연결 쌍 개수

# 인접 리스트 생성
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# BFS
visited = [False] * (n+1)
queue = deque([1])
visited[1] = True
count = 0

while queue:
    cur = queue.popleft()
    for nxt in adj[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            queue.append(nxt)
            count += 1

print(count)
