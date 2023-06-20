N, M = map(int, input().split())

while (N, M) != (0, 0):
  if N < M:
    if M % N == 0:
      print("factor")
    else:
      print("neither")
  elif N == M:
    print("neither")
  else:
    if N % M == 0:
      print("multiple")
    else:
      print("neither")
  N, M = map(int, input().split())