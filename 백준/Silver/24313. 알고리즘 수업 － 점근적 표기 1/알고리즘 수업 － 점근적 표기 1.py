import sys
a1, a0 = map(int,sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())


result = True
for n in range(n0, 101):
  if (n >= n0) & ((a1 * n + a0) <= (c * n)):
    result = True
  else:
    result = False
    break

if result:
  print(1)
else:
  print(0)