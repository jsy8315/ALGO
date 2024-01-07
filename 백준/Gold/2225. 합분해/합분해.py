import sys

data = list(map(int, sys.stdin.readline().split()))

N = data[0] # 0 ~ N 까지 더하기
K = data[1] # 정수 K개를 더해서 그 합이 N이 되야 함
#print(N)
#print(K)

dp = [0] * 201

for i in range(201):
  dp[i] = [1] * 201
  
for i in range(1, 201):
  dp[1][i] = i

if  N >= 2:
  for i in range(2, N + 1):
    for j in range(1, K + 1):
      dp[i][j] = sum(dp[i - 1][1:j + 1])
      #print("j는 " + str(j))
      #print(str(i) + "," + str(j) + "는 " + str(dp[i][j]))

print(dp[N][K] % 1000000000)