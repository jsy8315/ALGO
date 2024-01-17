import sys

N = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))
mvp = list(sys.stdin.readline().strip())


dp = [0] * N

if mvp[0] == "B":
  dp[0] = S[0] - 1
elif mvp[0] == "S":
  dp[0] = S[1] - 1
elif mvp[0] == "G":
  dp[0] = S[2] - 1
elif mvp[0] == "P":
  dp[0] = S[3] - 1
else:
  dp[0] = S[3]

for i in range(1, N):
  if mvp[i] == "B":
    dp[i] = S[0] - 1 - dp[i - 1]
  elif mvp[i] == "S":
    dp[i] = S[1] - 1 - dp[i - 1]
  elif mvp[i] == "G":
    dp[i] = S[2] - 1 - dp[i - 1]
  elif mvp[i] == "P":
    dp[i] = S[3] - 1 - dp[i - 1]
  else:
    dp[i] = S[3]

print(sum(dp))