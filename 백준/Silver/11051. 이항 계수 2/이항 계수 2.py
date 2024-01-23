import sys

N, K = map(int, sys.stdin.readline().split())



if K == 0:
  print(1)

else:
  A = N
  B = K

  for i in range(1, K):
    A = A * (N - i)

  for i in range(1, K):
    B = B * (K - i)
  print(int(A // B) % 10007)
