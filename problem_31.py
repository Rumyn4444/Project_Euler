coins = [1, 2, 5, 10, 20, 50, 100, 200]
dp = [0] * 201
dp[0] = 1
for coin in coins:
    for i in range(coin, 201):
        dp[i] += dp[i - coin]
print(dp[200])
