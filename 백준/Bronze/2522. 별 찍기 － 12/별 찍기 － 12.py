import sys

N = int(sys.stdin.readline())

for i in range(1, (2 * N)):
  if i < N + 1:
    print(
      ((" ") * (N - i)) +
      (("*") * i)
    )
  else:
    print(
      ((" ") * (i - N)) +
      (("*") * ((2 * N) - i))
    )
