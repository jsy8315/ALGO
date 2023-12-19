import sys

N = int(sys.stdin.readline())

if N == 1:
  result = 1
  print(result)
elif N == 2:
  result = 1
  print(result)
else: #N이 3이상인 경우부터 ㄱㄱ
  d = [[0] * 2 for _ in range(N + 1)]
  
  d[1] = [0, 1]
  d[2] = [1, 0]

  
  for i in range(3, N + 1):
    d[i][0] = d[i - 1][1] + d[i - 1][0]
    d[i][1] = d[i - 1][0]
    result = sum(d[i])
  print(result)