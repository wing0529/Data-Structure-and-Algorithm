import sys
import bisect
sys.stdin = open('C:\\Narae\\kw\\2025\\25-1\\자료구조와알고리즘\\HW1\\1920.txt','r')
N = int (input()) # list 크기
card = list(map(int,input().split()))
card.sort()# list 정렬
M = int(input())# target 크기 
target = list(map(int,input().split())) 

binary_results = []
def binary_search(t,card):
    left = 0
    right = len(card)-1

    while left <= right:
        mid = (left+right)//2
        if card[mid]==t:
            return 1
        elif card[mid] < t:
            left = mid + 1
        else:
            right = mid -1
    return 0
for i in range(M):
    t = target[i]
    binary_results.append(binary_search(t,card))
for r in binary_results:
    print(r)
