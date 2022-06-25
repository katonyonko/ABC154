import io
import sys

_INPUT = """\
6
100
1
25
2
314159
2
9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=list(input())
  N=[int(i) for i in N]
  n=len(N)
  K=int(input())
  dp=[[[0]*2 for j in range(K+1)] for i in range(n)]
  dp[0][0][0]=1
  dp[0][1][0]=N[0]-1
  dp[0][1][1]=1
  for i in range(n-1):
      for j in range(K+1):
          dp[i+1][j][0]+=dp[i][j][0]
          if j>0:
              dp[i+1][j][0]+=dp[i][j-1][0]*9
          if N[i+1]>0:
              dp[i+1][j][0]+=dp[i][j][1]
          if j>0 and N[i+1]>1:
              dp[i+1][j][0]+=dp[i][j-1][1]*(N[i+1]-1)
          if N[i+1]==0:
              dp[i+1][j][1]+=dp[i][j][1]
          if N[i+1]>0 and j>0:
              dp[i+1][j][1]+=dp[i][j-1][1]
  print(sum(dp[-1][-1]))