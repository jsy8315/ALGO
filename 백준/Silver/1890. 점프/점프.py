import sys

N = int(sys.stdin.readline())

A = [0] * N

for i in range(N):
  A[i] = list(map(int, sys.stdin.readline().split()))

dp = [[0] * N for _ in range(N)]

dp[0][0] = 1

for i in range(N):
  for j in range(N):
    if i == N - 1 and j == N - 1:
      print(dp[i][j])
      break

    K = A[i][j]

    if j + K < N:
      dp[i][j + K] += dp[i][j]

    if i + K < N:
      dp[i + K][j] += dp[i][j]
        
        
    
      