import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

dp = [0] * N
dp[0] = A[0]

if N == 1:
  print(A[0])
else:
  if A[1] > A[0] + A[1]:
    dp[1] = A[1]
  else:
    dp[1] = A[0] + A[1]
  
  for i in range(1, N):
    dp[i] = max(dp[i - 1] + A[i], A[i])
  
  print(max(dp))