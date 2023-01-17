'''
합분해 python 풀이
https://doctcoder.tistory.com/entry/%ED%95%A9%EB%B6%84%ED%95%B4-%ED%92%80%EC%9D%B4
'''
n,k=map(int,input().split())
dp=[[0 for i in range(k+1)] for j in range(n+1)]
dp[0][0]=1
for i in range(0,n+1):
	for j in range(1,k+1):
		dp[i][j]=dp[i][j-1]+dp[i-1][j]
print(dp[n][k]%1000000000)
