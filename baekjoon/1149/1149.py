'''
RGB거리 python 풀이
https://doctcoder.tistory.com/entry/RGB%EA%B1%B0%EB%A6%AC-%ED%92%80%EC%9D%B4
'''
n=int(input())
dp=[]
for i in range(n):
	dp.append(list(map(int,input().split())))
for i in range(1,n):
	dp[i][0]=min(dp[i-1][1],dp[i-1][2])+dp[i][0]
	dp[i][1]=min(dp[i-1][0],dp[i-1][2])+dp[i][1]
	dp[i][2]=min(dp[i-1][0],dp[i-1][1])+dp[i][2]
print(min(dp[n-1][0],dp[n-1][1],dp[n-1][2]))
