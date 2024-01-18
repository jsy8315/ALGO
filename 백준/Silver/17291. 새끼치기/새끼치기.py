import sys

N = int(sys.stdin.readline())

dp = [[0] * 21 for _ in range(21)]

dp[0] = [0]
dp[1] = [0, 1]
dp[2] = [0, 1, 1]
dp[3] = [0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
#dp[4] = [4, 2, 1]
#dp[5] = [7, 4, 2]

for i in range(4, N + 1):
  dp[i] = dp[i - 1]
  K = sum(dp[i - 1])

  if (i - 3) % 2 == 1:
    #i - 3년 꺼 삭제
    dp[i][i - 3] = 0
    
  if (i - 4) % 2 == 0:
    #i - 4년 꺼 삭제
    dp[i][i - 4] = 0

  dp[i][i] = K
  
print(sum(dp[N]))