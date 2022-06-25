import io
import sys

_INPUT = """\
6
5 3
1 2 2 4 5
4 1
6 6 6 6
10 4
17 13 13 12 15 20 10 13 17 11
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N, K = map(int, input().split())
  p=list(map(int,input().split()))

  for i in range(N):
    p[i]=(1+p[i])/2
    
  ans=[0]*(N-K+1)
  ans[0]=sum(p[:K])
  for i in range(1, N-K+1):
    ans[i]=ans[i-1]-p[i-1]+p[i+K-1]

  print(max(ans))