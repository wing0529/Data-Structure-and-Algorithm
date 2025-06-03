#백준 15649 N과 M (중간고사 100%)

'''
자연수 n과 m이 주어졌을때, 아래 조건을 만족하는 길이가 m인 수열을 모두 구하는 프로그램 작성 
조건 : 1부터 n까지 자연수 중에서 중복 없이 m개를 고른 수열

'''

def permute(ans):
    if len(ans)==m:
        print(*ans)
    else:
        for i in range(1,n+1):
            if i not in ans:
                ans.append(i)
                permute(ans)
                ans.pop()

n,m=map(int,input().split())
permute([])