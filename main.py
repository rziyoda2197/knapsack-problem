def knapsack(w, v, c):
    n = len(v)
    dp = [[0 for _ in range(c + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if w[i - 1] <= j:
                dp[i][j] = max(v[i - 1] + dp[i - 1][j - w[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][c]

w = [2, 3, 4, 5]
v = [10, 20, 30, 40]
c = 7

print(knapsack(w, v, c))
```

Kodni ishlatish uchun quyidagilar kerak:

- `w` - og'irliklar ro'yxati
- `v` - qiymatlar ro'yxati
- `c` - knapsack og'irlik chegarasi

Kod knapsack problemini halledadi va optimal qiymatni qaytaradi.
