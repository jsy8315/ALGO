import sys
N = int(sys.stdin.readline())

for i in range(1, (2 * N)):
  if i < N:
    print(
      (("*") * i) + 
      ((" ") * ((2 * N) - (2 * i))) + 
      (("*") * i)
    )
  elif i == N:
    print(
      ("*") * (2 * N)
    )
  else:
    print(
      (
        ("*") * ((2 * N) - i)
      ) + 
      (
        (" ") * (2 * (i - N))
      ) + 
      (
      ("*") * ((2 * N) - i)
      )
    )