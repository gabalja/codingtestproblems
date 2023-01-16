'''
1, 2, 3 더하기 5 python 풀이
https://doctcoder.tistory.com/entry/1-2-3-%EB%8D%94%ED%95%98%EA%B8%B0-5-%ED%92%80%EC%9D%B4
'''
dp=[[0 for i in range(3)]for j in range(100001)]
dp[1]=[1,0,0]
dp[2]=[0,1,0]
dp[3]=[1,1,1]
for i in range(4,100001):
	dp[i][0]=(dp[i-1][1]+dp[i-1][2])%1000000009
	dp[i][1]=(dp[i-2][0]+dp[i-2][2])%1000000009
	dp[i][2]=(dp[i-3][0]+dp[i-3][1])%1000000009

t=int(input())
for i in range(t):
	n=int(input())
	print(sum(dp[n])%1000000009)
