import sys
import math

N = int(sys.stdin.readline())
total = 0

#일단 짝수부터 
if N % 2 == 0:
  LN = (N // 2) + 1
    
else:
  #홀수하면
  LN = (N + 1) // 2

for i in range(LN):
  A = N - (2 * i)
  stepResult = math.comb(A + i, i)
  total = total + stepResult

result = total % 10007

print(result)