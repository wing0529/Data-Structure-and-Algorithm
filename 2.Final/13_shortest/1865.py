import sys
input = sys.stdin.readline

def bellman_ford(N, road):

    # 1) 큰 값으로 초기화
    directed_edge_count = 0
    for u in range(1, N + 1):
        directed_edge_count += len(road[u])
    BIG = directed_edge_count * 1000  # 최대 간선 개수 × 최대 가중치(≤1000)

    # 2) 거리 배열과 predecessor 배열 초기화 
    distance = [0] * (N + 1)
    predecessor = [None] * (N + 1)
    for i in range(1, N + 1):
        distance[i] = BIG
        predecessor[i] = None
    # 1번 vertex dist[1] = 0
    distance[1] = 0

    # 3) N-1번 반복 relax
    for _ in range(N - 1):
        updated = False
        for u in range(1, N + 1):
            if distance[u] == BIG:
                continue
            for v, w in road[u]:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    predecessor[v] = u
                    updated = True
        if not updated:
            break

    # 4) 음수 사이클 존재 여부 검사
    for u in range(1, N + 1):
        if distance[u] == BIG:
            continue
        for v, w in road[u]:
            if distance[u] + w < distance[v]:
                return False  # 음수 사이클이 존재

    return True  # 음수 사이클 없음


# ------------------ 메인 로직 ------------------
sys.stdin = open('C:\\Narae\\kw\\2025\\25-1\\class\\DSA\\Data-Structure-and-Algorithm\\2.Final\\13_shortest\\1865.txt', 'r')
input =sys.stdin.readline
tc = int(sys.stdin.readline())

for _ in range(tc):
    N, M, W = map(int, sys.stdin.readline().split())
    road = [[] for _ in range(N + 1)]

    # 1) 일반 도로 정보: 양방향, 가중치 T
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        road[S].append([E, T])
        road[E].append([S, T])

    # 2) 웜홀 정보: 단방향, 가중치 -T
    for _ in range(W):
        S, E, T = map(int, input().split())
        road[S].append([E, -T])#음수로 넣어줘야함 ! 

    # 3) Bellman-Ford로 음수 사이클 검사
    print(road)
    has_negative_cycle = bellman_ford(N, road)

    # 4) 결과 출력
    print("No" if has_negative_cycle else "Yes")


