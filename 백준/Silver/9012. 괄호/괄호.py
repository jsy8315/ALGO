import sys

N = int(sys.stdin.readline().rstrip())

count = 0
result1 = "NO"
result2 = 0

while (count < N):
  result2 = 0
  arr = list(sys.stdin.readline().rstrip())
  countR = 0
  countL = 0
  for i in range(len(arr)):
    if arr[i] == '(':
      countL = countL + 1

    else:
      countR = countR + 1


    if countL < countR:
      result2 = 1

  if (countR == countL) and arr[0] == '(' and arr[-1] == ')' and result2 == 0:
    print("YES")
  else:
    print("NO")
  count = count + 1
