import sys
sys.stdin=open('C:\\Narae\\kw\\2025\\25-1\\class\\DSA\\Data-Structure-and-Algorithm\\Final\\11_dynamic\\2748.txt','r')
n = int(input())

def fibonacci(n):
    if n<2:
        return n
    if _memo[n] is None:
        _memo[n]=fibonacci(n-1)+fibonacci(n-2)
    return _memo[n]

_memo = [None]*90


print(fibonacci(n))


def fibonacci_bu(n):
    memo = [0,1]

    for i in range(2,n+1):
        memo.append(memo[i-1]+memo[i-2])

    return memo[-1]

print(fibonacci_bu(n))
