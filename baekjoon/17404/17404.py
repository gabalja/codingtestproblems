'''
RGB거리 2 python 풀이
https://doctcoder.tistory.com/entry/RGB%EA%B1%B0%EB%A6%AC-2-%ED%92%80%EC%9D%B4
'''
n=int(input())
arr=[]
inf=10000
res=inf
for i in range(n):
	arr.append(list(map(int,input().split())))
dp=[[0]*3 for i in range(2)]
for i in range(3):
	dp[0][0],dp[0][1],dp[0][2]=inf,inf,inf
	dp[0][i]=arr[0][i]
	for j in range(1,n):
		dp[1][0]=min(dp[0][1],dp[0][2])+arr[j][0]
		dp[1][1]=min(dp[0][0],dp[0][2])+arr[j][1]
		dp[1][2]=min(dp[0][0],dp[0][1])+arr[j][2]
		dp[0][0],dp[0][1],dp[0][2]=dp[1][0],dp[1][1],dp[1][2]
	res=min(res,min(dp[0][(i+1)%3],dp[0][(i+2)%3]))
print(res)
