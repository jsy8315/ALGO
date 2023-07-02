import sys

N = int(sys.stdin.readline().rstrip())

arr = []

for i in range(N):
  k = int(sys.stdin.readline().rstrip())
  arr.append(k)


#1부터 N까지 수열인데 거꾸로 정렬해서 stack 사용할거임
oriArr = []
for i in range(1, N + 1):
  oriArr.append(N + 1 - i)


#midStack에 넣을때 오름차순 push해야됨
midStack = []
#finalStack에 넣을때 pop으로 넣
finalStack = []

printResult = []

for i in range(1, arr[0] + 1):
  oriArr.pop()
  midStack.append(i)
  printResult.append("+")

finalStack.append(midStack[-1])
midStack.pop()
printResult.append("-")

Result = 0


for i in range(1, N):
  if arr[i - 1] > arr[i]:
    if arr[i] == midStack[-1]:
      finalStack.append(midStack[-1])
      midStack.pop()
      printResult.append("-")
    else:
      Result = 1
      break
  elif arr[i - 1] < arr[i]:
    while True:
      midStack.append(oriArr[-1])
      printResult.append("+")
      oriArr.pop()
      if midStack[-1] == arr[i]:
        break
    finalStack.append(midStack[-1])
    midStack.pop()
    printResult.append("-")

if Result == 1:
  print("NO")
else:
  print(*printResult, sep='\n')