import sys
from bisect import bisect_left

sys.stdin = open('C:\\Narae\\kw\\2025\\25-1\\class\\DSA\\Data-Structure-and-Algorithm\\2.Final\\12_greedy\\1931.txt', 'r')
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 할당
n = int(input().strip())  # 첫 줄: 회의 개수

acts = []
for _ in range(n):
    a, b = map(int, input().split())
    acts.append((a, b))
    # a: 시작 시간, b: 종료 시간

# 2) 종료 시간 기준 오름차순, 종료 시간이 같으면 시작 시간 기준 오름차순으로 정렬
acts.sort(key=lambda x: (x[1], x[0]))

# 시작 시간과 종료 시간을 각각 분리해서 리스트로
starts = [act[0] for act in acts]
ends = [act[1] for act in acts]

# 3) 각 활동 i에 대해 'i번 활동을 끝낸 뒤 선택할 수 있는 다음 인덱스(next_idx)'를 미리 계산 → ends[i] 이후에 시작하는 활동 중에서 가장 이른 인덱스를 찾기 위해 이진 탐색 사용
next_idx = [0] * n
for i in range(n):
    # bisect_left(starts, ends[i])는 'ends[i]' 이상인 첫 시작 인덱스를 찾음
    j = bisect_left(starts, ends[i])
    next_idx[i] = j  # j가 n이면 이후에 고를 활동이 없다는 의미

# 4) 바텀업 DP를 위한 배열
#    dp[i] = i번 활동부터 끝까지 고를 수 있는 최대 회의 개수, 
#    dp[n] = 0 (베이스 케이스: 인덱스가 n 이상이면 더 이상 고를 게 없음)
dp = [0] * (n + 1)

# 5) 바텀업 채우기 (i = n-1부터 0까지)
for i in range(n - 1, -1, -1):
    # 1) i번 회의를 선택하지 않는 경우: dp[i+1]
    skip = dp[i + 1]
    # 2) i번 회의를 선택하는 경우: 1 + dp[next_idx[i]]
    take = 1 + dp[next_idx[i]]
    # 둘 중 최댓값을 dp[i]에 저장
    dp[i] = max(skip, take)

# 6) 결과 출력: dp[0]이 0번 활동부터 최대로 고른 개수
print(dp[0])
