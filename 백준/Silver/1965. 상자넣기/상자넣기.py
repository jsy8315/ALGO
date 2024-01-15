import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

a.insert(0, 0)

dp = [0] * (n + 1)

for i in range(1, n + 1):
  dp[i] = 1

for i in range(1, n + 1):
  for j in range(1, i):
    if a[i] > a[j]:
      dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))