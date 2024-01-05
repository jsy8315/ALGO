import sys

N = int(sys.stdin.readline())

dp = [0] * 31
dp[2] = 3
dp[4] = 11

for i in range(N + 1):
  if i % 2 == 1:
    dp[i] = 0
  else:
    dp[2] = 3
    dp[4] = 11

if N >= 6:
  for i in range(6, N + 1, 2):
    midSum = sum(dp[:i - 2])
    dp[i] = 2 + dp[i - 2] * dp[2] + midSum * 2

print(dp[N])