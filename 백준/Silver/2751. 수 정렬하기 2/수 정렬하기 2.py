import sys
N = int(sys.stdin.readline())
arr = [0] * 2000001

for i in range(N):
  a = int(sys.stdin.readline())
  arr[a + 1000000] += 1

for i in range(2000001):
  if arr[i] != 0:
    for j in range(arr[i]):
      print(i - 1000000)