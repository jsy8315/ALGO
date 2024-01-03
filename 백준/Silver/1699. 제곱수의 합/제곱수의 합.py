import sys

N = int(sys.stdin.readline())

dp = [i for i in range(N + 1)] #모든 수는 "1"만으로 구성되어 있을때, 값만큼 길이를 가짐

for i in range(1, N + 1):
  for j in range(1, i):
    if j * j > i:
      break
    if dp[i] > dp[i - j * j] + 1:
      dp[i] = dp[i - j * j] + 1
print(dp[N])