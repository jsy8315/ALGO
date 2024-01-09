import sys

N = int(sys.stdin.readline())

dp = [2] * (1001)
#dp는 돌을 가져가는 횟수
dp[1] = 1
dp[2] = 2
dp[3] = 1
dp[4] = 1

for i in range(5, 1001):
  if ((1 + dp[i - 4] ) % 2 == 1) or ((1 + dp[i - 3] ) % 2 == 1) or ((1 + dp[i - 1] ) % 2 == 1):
    dp[i] = 1

if dp[N] % 2 == 1:
  print("SK")
else:
  print("CY")
    