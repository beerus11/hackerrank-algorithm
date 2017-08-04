m,n=map(int,raw_input().split(" "))
c=map(int,raw_input().split(" "))
c.sort()
dp=[[0]*(m+1) for i in range(len(c)+1)]
for i in range(len(c)+1):
	for j in range(m+1):
		if i==0:
			dp[i][j]=0
		if j==0:
			dp[i][j]=1
			
for i in range(1,len(c)+1):
	for j in range(1,m+1):
		if c[i-1]>j:
			dp[i][j]=dp[i-1][j]
		else:
			dp[i][j]=dp[i][j-c[i-1]]+dp[i-1][j]
print dp[len(c)][m]
