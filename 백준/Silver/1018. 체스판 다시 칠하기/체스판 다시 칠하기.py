import sys

N, M = map(int, sys.stdin.readline().split())
board = [input() for _ in range(N)]

count = 0

chessB = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']

chessW = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']

countBR = []
countWR = []

#N a는 0부터 2
#M b는 0부터 5

for a in range(N - 7):
  for b in range(M - 7):
    count = 0
    for i in range(8):
      for j in range(8):
        if chessB[i][j] != board[i + a][j + b]:
          count += 1
        else:
          continue    
    countBR.append(count)

bb = min(countBR)

for a in range(N - 7):
  for b in range(M - 7):
    count = 0
    for i in range(8):
      for j in range(8):
        if chessW[i][j] != board[i + a][j + b]:
          count += 1
        else:
          continue
    countWR.append(count)

ww = min(countWR)

print(min(bb, ww))