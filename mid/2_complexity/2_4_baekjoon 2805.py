# 백준 2805 - 나무 자르기 (Binary Search)

import sys 

#sys.stdin = open('bj2805.txt','r')  # 로컬 테스트용 파일 입력

# 입력 처리
n, m = map(int, input().split())                # n: 나무 수, m: 필요한 나무 길이
woods = list(map(int, input().split()))         # woods: 나무 높이 리스트

# 이진 탐색 범위 설정 (절단기 높이 범위)
left, right = 0, max(woods) # 최소 =0, 최대= 가장 큰 나무의 길이

while left <= right:# right가 left보다 크거나 같은 경우 계속 루프 진행
    mid = (left + right) // 2                   # 절단기 높이 후보

    h = 0  # 이번 mid 높이에서 잘린 나무 총합
    for w in woods:#나무의 길이를 각각 mid와 비교
        if w >= mid:
            h += w - mid  # 잘린 만큼 누적

    if h >= m:
        # 잘린 양이 충분함 → 절단기 높이 더 높일 수 있음
        left = mid + 1
    else:
        # 잘린 양이 부족함 → 절단기 높이 낮춰야 함
        right = mid - 1

# 최종 조건을 만족하는 최대 절단기 높이 출력
print(right)
