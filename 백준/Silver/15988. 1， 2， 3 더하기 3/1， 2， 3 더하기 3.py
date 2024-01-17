import sys

T = int(sys.stdin.readline())
A = [0] * (T + 1)


for i in range(1, T + 1):
  B = int(sys.stdin.readline())
  A[i] = B

dp = [0] * (1000001)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000001):
  dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3])% 1000000009
    
for i in range(1, T + 1):
  print(dp[A[i]] )