'''
쉬운 계단 수 python 풀이
https://doctcoder.tistory.com/entry/%EC%89%AC%EC%9A%B4-%EA%B3%84%EB%8B%A8-%EC%88%98-%ED%92%80%EC%9D%B4
'''
dp=[[0 for i in range(10)] for j in range(101)]
for i in range(1,10):
	dp[1][i]=1
n=int(input())
for i in range(2,n+1):
	for j in range(10):
		if j==0: dp[i][j]=dp[i-1][1]
		elif j==9: dp[i][j]=dp[i-1][8]
		else: dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]
print(sum(dp[n])%1000000000)
