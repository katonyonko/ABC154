import io
import sys

_INPUT = """\
6
sardine
xxxx
gone
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S = input()
  l=len(S)
  print("x"*l)