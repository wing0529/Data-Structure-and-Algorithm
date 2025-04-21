# 백준 10825 - 국영수 (파일 입력 테스트용, sys.stdin 설정 O)

import sys
sys.stdin = open('bj10825.txt', 'r')  # 테스트용 파일 열기
input = sys.stdin.readline            # 빠른 입력으로 교체, input()으로 하면 시간이 오래걸림

n = int(input())
data = []

for _ in range(n):
    name, kor, eng, math = input().split()
    data.append((name, int(kor), int(eng), int(math)))

data.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for d in data: # 1줄로 코딩 가능 
    print(d[0])

print('\n'.join(d[0] for d in data)) # 1줄로 코딩 

# 백준 10825 - 국영수 (백준 제출용, 키보드 입력 전용)

import sys
input = sys.stdin.readline  # 빠른 입력 사용

n = int(input())
data = []

for _ in range(n):
    name, kor, eng, math = input().split()
    data.append((name, int(kor), int(eng), int(math)))

data.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for d in data: # 1줄로 코딩 가능 
    print(d[0])

# 1줄로 코딩 가능 
print('\n'.join([d[0] for d in data]))# 리스트 
print('\n'.join(d[0] for d in data))# 제너레이터 - 더 효율적 ! 메모리 절약