# Linear search
import sys 

#sys.stdin = open('bj1920.txt','r')

# 입력 처리
N = int(input()) # 자연수 개수
card = list(map(int, input().split())) # list
card.sort()
M = int(input()) # target 개수 
target = list(map(int, input().split())) # 각 target 값 들

def linear_search(unordered_list, compare):
    for x in unordered_list:
        if x == compare:
            return True
        else:
            return None

# 결과 출력
for i in target:
    result = linear_search(card, i)
    if result is None:
        print(0)
    else:
        print(1)


