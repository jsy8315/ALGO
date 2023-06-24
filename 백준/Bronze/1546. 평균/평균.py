import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
c = sorted(arr,reverse=True)

M = int(c[0])
hap = 0

for i in range(N):
  arr[i] = int(arr[i]) / M * 100

print(sum(arr) / N)