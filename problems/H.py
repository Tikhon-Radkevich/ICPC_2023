MOD = 998244353

def min_value_and_count(n, W, a, p):
    dp = [0] * (W + 1)
    dp[0] = 1

    for i in range(n):
        for w in range(W, -1, -1):
            if w - a[i] >= 0:
                dp[w] += dp[w - a[i]]
                dp[w] %= MOD

    if dp[W] == 0:
        return -1
    else:
        count = dp[W]
        min_val = sum(p[i] for i in range(n) if W >= a[i]) % MOD
        return min_val, count

n, W = map(int, input().split())
a = list(map(int, input().split()))
p = list(map(int, input().split()))

result = min_value_and_count(n, W, a, p)
if result == -1:
    print("-1")
else:
    print(*result)
