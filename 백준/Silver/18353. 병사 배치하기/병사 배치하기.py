import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

#dp[i]는 i - 1번째에서 남아있는 최대 병사의 수

dp = [1] * N

for i in range(1, N):
  for j in range(i):
    if A[j] > A[i]:
      dp[i] = max(dp[j] + 1, dp[i])

print(N - max(dp))

