import io
import sys

_INPUT = """\
6
5
2 6 1 4 5
6
4 1 3 1 6 2
2
10000000 10000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N = int(input())
  A = list(map(int, input().split()))

  s=set()
  for i in range(N):
    s.add(A[i])
    
  if len(s)==N:
    print("YES")
  else:
    print("NO")