import sys

N, K = map(int, sys.stdin.readline().split())

resultK = 1
resultN = 1
resultNK = 1

if K == 0:
  print(1)
else:
  for i in range(1, K + 1):
    resultK = resultK * i

  for i in range(1, N + 1):
    resultN= resultN * i

  for i in range(1, N - K + 1):
    resultNK= resultNK * i

  print(resultN // ((resultK) * resultNK))