import io
import sys

_INPUT = """\
6
1 1 2 2
314 159 2653 589
1 3 4 1000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=10**9+7
  N=2*10**6
  F=[1]
  for i in range(N):
    F.append(F[-1]*(i+1)%mod)
  I=[pow(F[-1],mod-2,mod)]
  for i in range(N):
    I.append(I[-1]*(N-i)%mod)
  I=I[::-1]
  r1,c1,r2,c2=map(int,input().split())
  def FF(r,c):
    res=0
    tmp=1
    for i in range(r+c+1):
      res=(res+tmp)%mod
      tmp=(tmp*2)%mod
      if i>=r: tmp=(tmp-F[i]*I[r]*I[i-r])%mod
      if i>=c: tmp=(tmp-F[i]*I[c]*I[i-c])%mod
    return res
  print((FF(r2,c2)-FF(r1-1,c2)-FF(r2,c1-1)+FF(r1-1,c1-1))%mod)