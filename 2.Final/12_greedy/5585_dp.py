import sys
input = sys.stdin.readline

def min_coins(money, coins):
    change = 1000 - money
    # dp[i] = i원을 거슬러 줄 때 필요한 최소 동전 개수
    # 초기값: 충분히 큰 수(여기서는 amount+1 이상이면 못 만드는 의미)
    dp = [change + 1] * (change + 1)
    dp[0] = 0  # 0원을 거슬러 줄 땐 동전 0개

    # 바텀업 채우기
    for coin in coins:
        for current in range(coin, change + 1):
            # dp[current]는 기존 값 vs dp[current - coin] + 1 중 Min
            dp[current] = min(dp[current], dp[current - coin] + 1)

    return dp[change]

# 사용자가 지불한 금액 money (0 ≤ money ≤ 1000)
money = int(input().strip())

# 동전 단위 
coins = [500, 100, 50, 10, 5, 1]

# 거스름돈 계산


#최소 동전 개수 
answer = min_coins(money, coins)

print(answer)
