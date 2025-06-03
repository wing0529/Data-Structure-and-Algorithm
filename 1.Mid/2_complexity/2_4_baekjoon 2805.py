# 백준 2805 - 나무 자르기 (Binary Search with h 저장)

import sys
# sys.stdin = open('bj2805.txt', 'r')  # 로컬 테스트용

# 입력 처리
n, m = map(int, input().split())
woods = list(map(int, input().split()))

# 이진 탐색 범위 설정
left, right = 0, max(woods)
h = left  # 현재 톱의 높이를 저장할 변수

while left <= right:
    mid = (left + right) // 2  # 절단기 높이 후보

    total = 0  # 잘린 나무 총합
    for w in woods:
        if w > mid:
            total += w - mid

    if total >= m:
        h = mid          # 조건 만족 → 현재 높이 저장
        left = mid + 1   # 더 높여볼 수 있음
    else:
        right = mid - 1  # 자른 양 부족 → 낮춰야 함

# 최종적으로 조건을 만족하는 최대 절단기 높이 출력
print(h)
