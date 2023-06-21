N,M = map(int, input().split())

arr = [];

for i in range(1,N+1):
  arr.append(i)

for i in range(0, M):
  A, B = map(int, input().split())
  if A == B :
    continue
  else :
    c = arr[A - 1]
    arr[A - 1] = arr[B - 1]
    arr[B - 1] = c


for i in range(0,N):
  print(arr[i], end=' ')