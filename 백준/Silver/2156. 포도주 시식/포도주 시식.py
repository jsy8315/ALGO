import sys

n = int(sys.stdin.readline())

data = [int(sys.stdin.readline().strip()) for i in range(n)]


total = [0] * n
total[0] = data[0]

if n > 1:
  total[1] = data[0] + data[1]

if n > 2:
  total[2] = max(total[1], data[2] + data[1], data[2] + data[0])

for i in range(3, n):
  total[i] = max(total[i - 1], data[i] + data[i - 1] + total[i - 3], data[i] + total[i - 2])

print(total[n - 1])