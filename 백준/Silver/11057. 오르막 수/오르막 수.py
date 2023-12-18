import sys

N = int(sys.stdin.readline())

d = [[0] * 10 for _ in range(N + 1)]

d[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#d[2] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in range(2, N + 1):
  for j in range(10):
    stepSum = 0
    for k in range(j, 10):
      #d[i][j] = d[i - 1][k]까지 다 더한거
      stepSum += d[i - 1][k]
    d[i][j] = stepSum


result = sum(d[N])
print(result % 10007)
  

