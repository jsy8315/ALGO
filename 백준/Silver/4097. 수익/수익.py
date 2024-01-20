import sys

while True:
  N = int(sys.stdin.readline())
  if N == 0:
    break

  dp = []
  for i in range(N):
    dp.append(int(sys.stdin.readline()))
    
  for i in range(1, N):
    dp[i] = max(dp[i], dp[i - 1] + dp[i])
  print(max(dp))

  

