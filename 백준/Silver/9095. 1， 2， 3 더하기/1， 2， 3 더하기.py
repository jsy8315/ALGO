import sys

T = int(sys.stdin.readline())
inputStrData = [sys.stdin.readline().strip() for i in range(T)]

#리스트 형식의 str로 입력받은 값을 int로 변환
inputIntData = list(map(int, inputStrData))

d = [0]
d.append(1)
d.append(2)
d.append(4)

#print("------inputIntData의 값--------")
#print(inputIntData)
#print("------------d의 값-------------")
maxData = max(inputIntData)

for i in range(4, maxData + 1):
  d.append(d[i - 1] + d[i - 2] + d[i - 3])
  
#print(d)

for i in range(T):
  for j in range(maxData):
    if inputIntData[i] == j + 1:
      print(d[j + 1])



  
  
