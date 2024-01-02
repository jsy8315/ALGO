import sys

N = int(sys.stdin.readline())

stairs= []

for i in range(N):
  stairs.append(int(sys.stdin.readline()))
#print(stairs)

dp = [0] * N
dp[0] = stairs[0]
#print(dp)

if N > 3:
  dp[1] = stairs[0] + stairs[1]
  dp[2] = max((stairs[0] + stairs[2]), (stairs[1] + stairs[2]))
  for i in range(3, N):
    dp[i] = max((dp[i - 2] + stairs[i]), (dp[i - 3] + stairs[i - 1] + stairs[i]))
    #print(dp)
  print((dp[-1]))
  
elif N == 3:
  dp[1] = stairs[0] + stairs[1]
  dp[2] = max((stairs[0] + stairs[2]), (stairs[1] + stairs[2]))
  print(dp[2])
  
elif N == 2:
  dp[1] = stairs[0] + stairs[1]
  print(dp[1])
  
else:
  print(dp[0])
