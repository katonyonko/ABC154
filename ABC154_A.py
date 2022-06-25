import io
import sys

_INPUT = """\
6
red blue
3 4
red
red blue
5 5
blue
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S, T = input().split()
  A, B = map(int, input().split())
  U = input()

  if S==U:
    print(A-1, B)
  else:
    print(A, B-1)