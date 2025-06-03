import sys

def selector(activities):
    """
    정렬된 활동 목록을 받아서 그리디하게 최대 개수를 선택하는 함수.
    activities: [(start1, end1), (start2, end2), …] 형태로,
                종료 시간을 기준으로 오름차순, 종료 시간이 같으면 시작 시간을 기준으로 오름차순 정렬돼 있어야 함.
    반환값: 선택할 수 있는 최대 활동 개수
    """
    count = 0
    last_end = 0

    for start, end in activities:
        # 현재 활동의 시작 시간이 마지막으로 선택된 활동의 종료 시간보다 크거나 같으면 선택 가능
        if start >= last_end:
            count += 1
            last_end = end

    return count

# ------------------ 입력 처리 ------------------

# 1) 테스트용으로 텍스트 파일을 읽도록 설정
#    (백준에 제출할 땐 이 줄을 주석 처리하거나 삭제하고, input()을 사용하세요)
sys.stdin = open('C:\\Narae\\kw\\2025\\25-1\\class\\DSA\\Data-Structure-and-Algorithm\\2.Final\\12_greedy\\1931.txt', 'r')
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 할당

n = int(input().strip())  # 첫 줄: 회의 개수

acts = []
for _ in range(n):
    a, b = map(int, input().split())
    acts.append((a, b))
    # a: 시작 시간, b: 종료 시간

# 2) 종료 시간 기준 오름차순, 종료 시간이 같으면 시작 시간 기준 오름차순으로 정렬
#    → 이 순서대로 그리디 선택하면 최대 회의 수를 고를 수 있음
acts.sort(key=lambda x: (x[1], x[0]))

# ------------------ 결과 출력 ------------------
print(selector(acts))

