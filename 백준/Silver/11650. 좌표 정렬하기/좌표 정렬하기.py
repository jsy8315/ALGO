import sys

N = int(sys.stdin.readline())

spot = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

spot.sort(key=lambda x: (x[0], x[1]))

for i in spot:
  for j in i:
    print(j, end=' ')
  print()