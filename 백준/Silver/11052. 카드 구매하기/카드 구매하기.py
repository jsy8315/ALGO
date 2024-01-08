import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
A.insert(0, 0)

for i in range(1, N + 1):
  for j in range(1, i):
    A[i] = max(A[i], A[i - j] + A[j])

print(max(A))