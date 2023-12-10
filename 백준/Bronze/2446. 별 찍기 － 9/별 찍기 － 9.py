import sys

N = int(sys.stdin.readline())
M = 2 * N - 1

for i in range((2 * N) - 1):
  if i < N:
    print(
      ((" ") * i) +
      (("*") * (M - (2 * i))) +
      (("") * i) 
    )
  else:
    print(
      ((" ") * (M - 1 - i)) +
      (("*") * (M - (2 * ((M - 1) - i)))) +
      (("") * (M - 1 - i))
    )