import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

dp = [1] * N


for i in range(1, N):
  for j in range(i):
    if A[i] > A[j]:
      dp[i] = max(dp[i], dp[j] + 1)
#print("증가 부분")
#print(dp)

dp2 = [1] * N

for i in range(N - 1, -1, -1):
  for j in range(N - 1, i, -1):
    if A[i] > A[j]:
      dp2[i] = max(dp2[i], dp2[j] + 1)
#print("감소 부분")
#print(dp2)

for i in range(N):
  dp[i] += dp2[i] - 1
  
#print("증가 + 감소 부분")
#print(dp)

print(max(dp))