import sys

N = int(sys.stdin.readline())

d = [0] * 1001

for i in range(3, 1001):
  d[0] = 0
  d[1] = 1
  d[2] = 3
  d[i] = d[i - 1] + (2 * (d[i - 2]))

result = d[N] % 10007
print(result)