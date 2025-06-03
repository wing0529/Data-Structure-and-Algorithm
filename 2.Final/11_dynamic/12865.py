import sys

# 1) n(아이템 개수), k(배낭 용량) 입력
sys.stdin=open('C:\\Narae\\kw\\2025\\25-1\\class\\DSA\\Data-Structure-and-Algorithm\\Final\\11_dynamic\\12865.txt','r')
n, k = map(int, sys.stdin.readline().split())


# 2) info: 아이템 정보를 저장할 딕셔너리
# info[i] = (weight_i, value_i)
info = {}
for i in range(n):
    w, v = map(int, input().split())
    info[i] = (w, v)

# 3) _memo: (capacity, item_index) 상태 → 최대 가치를 저장하는 딕셔너리 (메모이제이션 캐시)
_memo = {}

def knapsack(capacity, item_index):
    """
    capacity:   남은 배낭 용량 (0 <= capacity <= k)
    item_index: 현재 고려 중인 아이템 인덱스 (0 <= item_index < n)

    반환값: 해당 상태(capacity, item_index)에서 얻을 수 있는 최대 가치 (int)
    """
    # 기저 조건: 용량이 0이거나, 모든 아이템을 다 고려했으면 0 반환
    if capacity == 0 or item_index >= n:
        return 0

    # item_index에 대한 캐시 딕셔너리가 없으면 생성
    if item_index not in _memo:
        _memo[item_index] = {}

    # 이미 계산된 상태라면, _memo[item_index][capacity]를 바로 반환
    if capacity in _memo[item_index]:
        return _memo[item_index][capacity]

    w_i, v_i = info[item_index]

    # (1) 이 아이템을 담을 수 없으면 건너뛰기
    if w_i > capacity:
        result = knapsack(capacity, item_index + 1)
    else:
        # (2-1) 담는 경우
        take = v_i + knapsack(capacity - w_i, item_index + 1)
        # (2-2) 담지 않는 경우
        skip = knapsack(capacity, item_index + 1)
        result = max(take, skip)

    # 계산된 결과를 메모이제이션 딕셔너리에 저장
    _memo[item_index][capacity] = result
    return result

# 4) 최종 결과 출력: 배낭 용량 k, 0번 아이템부터 시작
print(knapsack(k, 0))