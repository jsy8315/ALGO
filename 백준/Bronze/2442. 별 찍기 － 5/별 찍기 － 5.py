import sys
N = int(sys.stdin.readline())

for i in range(N):
  print((" " * (N - 1 -i)) + ("*" * ((2 * (i + 1)) - 1)) + ("" * (N - 1 -i)))