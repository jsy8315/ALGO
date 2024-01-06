import sys

data = []
T = int(sys.stdin.readline())

for i in range(T):
  data.append(int(sys.stdin.readline()))


dp = [0] * (101)
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(6, 101):
  dp[i] = dp[i - 2] + dp[i - 3]

for j in range(T):
  print(dp[data[j]])