#먼저 입력값 받고
str = input()

#모두 대문자로 변환
str = str.upper()

#대문자 알파벳이 모두 있는 리슽 배열 선언
STR = [
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

count = [
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

#26자리로 구성된 count을 선언해, 나오는 알파벳 숫자를 요소로 바꿔버리기
for i in str:
  a = 0
  for j in STR:
    if i == j:
      count[a] += 1
    else:
      a += 1

#정렬해서 중복값 있는지 체크, 없으면 진행

if len(str) == 1:
  print(str)
else:
  #오름차순 정렬
  descCount = sorted(count)
  if descCount[-1] == descCount[-2]:
    print("?")
  else:
    max(count)
    for i in range(0,26):
      if count[i] == max(count):
        print(STR[i])