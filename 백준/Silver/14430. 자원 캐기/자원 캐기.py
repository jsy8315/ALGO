import sys

NM = list(map(int, sys.stdin.readline().split()))

N = NM[0] #세로길이
M = NM[1] #가로길이
A = [0] * N

for i in range(N):
  B = list(map(int, sys.stdin.readline().split()))
  A[i] = B

dp = [[0] * M for _ in range(N)]
dp[0][0] = A[0][0]

for j in range(1, M):
  dp[0][j] = dp[0][j - 1] + A[0][j]

for i in range(1, N):
  dp[i][0] = dp[i - 1][0] + A[i][0]

for i in range(1, N):
  for j in range(1, M):
    dp[i][j] = max(dp[i - 1][j] + A[i][j], dp[i][j - 1] + A[i][j])

print(max(max(dp)))