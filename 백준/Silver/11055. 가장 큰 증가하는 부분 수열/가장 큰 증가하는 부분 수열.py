import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

#11053번이랑 다르게 dp는 뭘 의미하도록 해야되지?
#수열의 합으로 해볼까?
dp = [0] * N
dp[0] = A[0] #dp의 첫번째 값은 수열 A와 동일

for i in range(1, N):
  dp[i] = A[i]
#print(dp)

for i in range(1, N):
  for j in range(i):
    if A[i] > A[j]:
      dp[i] = max(dp[i], dp[j] + A[i])
      #print(dp)

print(max(dp))

