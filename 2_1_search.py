# Binary search using bisect
import sys 
import bisect

#sys.stdin = open('bj1920.txt','r')

# 입력 처리
N = int(input()) # 자연수 개수
card = list(map(int, input().split())) # list
card.sort()
M = int(input()) # target 개수 
target = list(map(int, input().split())) # 각 target 값 들

def binary_search(ordered_list, compare):
    index = bisect.bisect_left(ordered_list,compare)

    if index < len(ordered_list) and ordered_list[index]==compare:
        return index
    else:
        return None

# 결과 출력
for i in target:
    result = binary_search(card, i)
    if result is None:
        print(0)
    else:
        print(1)


