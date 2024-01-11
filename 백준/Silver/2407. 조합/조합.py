import sys

A = list(map(int, sys.stdin.readline().split()))

n = A[0]
m = A[1]

dpN = [1] * (n + 1)
dpM = [1] * (m + 1)

resultN = 1
resultM = 1

for i in range(n - m + 1, n + 1):
  dpN[i] = i
  resultN = resultN * dpN[i]

for i in range(1, m + 1):
  dpM[i] = i
  resultM = resultM * dpM[i]

print(resultN // resultM)