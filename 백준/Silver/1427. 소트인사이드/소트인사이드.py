import sys
arr = list(map(int, sys.stdin.readline().strip()))
c = sorted(arr,reverse=True)
for i in c:
  print(i, end="")