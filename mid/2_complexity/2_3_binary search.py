# Binary search
import sys 

#sys.stdin = open('bj1920.txt','r')

# 입력 처리
N = int(input()) # 자연수 개수
card = list(map(int, input().split())) # list
card.sort()
M = int(input()) # target 개수 
target = list(map(int, input().split())) # 각 target 값 들

def binary_search(ordered_list, compare):
    left =0
    right = len(ordered_list)-1

    while left <= right:
        mid = (left+right)//2
        if ordered_list[mid]==compare:
            return True
        elif ordered_list[mid]<compare:
            left = mid+1
        else:
            right = mid -1
    return None

# 결과 출력
for i in target:
    result = binary_search(card, i)
    if result is None:
        print(0)
    else:
        print(1)


