
#백준 15650 N과 M (중간고사 100%)

'''
자연수 n과 m이 주어졌을때, 아래 조건을 만족하는 길이가 m인 수열을 모두 구하는 프로그램 작성 
조건 : 1부터 n까지 자연수 중에서 중복 없이 m개를 고른 수열
조건 : 고른 수열은 오름 차순 이어야 한다.
'''

def combine1(ans):
    if len(ans)==m:
        print(*ans)
    else:
        for i in range(1,n+1):
            if not ans or i > ans[-1]:
                if not ans or i > ans[-1]:
                # - ans가 비어 있다면 무조건 OK
                # - ans가 비어 있지 않다면 "오름차순 조건(i > 마지막 원소)"을 만족해야만 append()
                # → 이 조건 하나로 **중복 없이 오름차순 조합**을 만들 수 있음
                    ans.append(i)
                    combine1(ans)
                    ans.pop()
5

# 교수님 정답 코드 !
def combine2(ans):
    if len(ans)==m:
        print(*ans)
    else:
        for i in range(1,n+1):
            if len(ans)>0  and i <= ans[-1]:# 비어있는거 방지 + 중복을 걸러줌 
                # ans가 비어있지 않으면서 i가 이전 값보다 작거나 같으면 skip
                # → 오름차순 보장 + 중복도 자연스럽게 방지됨
                continue
            else:
                ans.append(i)
                combine2(ans)
                ans.pop()


n,m = map(int,input().split())
combine1([])
combine2([])
