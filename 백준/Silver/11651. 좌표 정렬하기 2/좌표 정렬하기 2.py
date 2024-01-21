import sys

N = int(sys.stdin.readline())

A = [0] * N

for i in range(N):
  K = list(map(int, sys.stdin.readline().split()))
  A[i] = K

B = sorted(A, key = lambda x : (x[1], x[0]))
for i in range(N):
  print(B[i][0], B[i][1])