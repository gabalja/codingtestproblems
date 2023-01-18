'''
연속합 2 python 풀이
https://doctcoder.tistory.com/entry/%EC%97%B0%EC%86%8D%ED%95%A9-2-%ED%92%80%EC%9D%B4
'''
n=int(input())
arr=list(map(int,input().split()))
dp=[[i for i in arr] for j in range(2)]
for i in range(1,n):
	dp[0][i]=max(dp[0][i-1]+arr[i],dp[0][i])
	dp[1][i]=max(dp[0][i-1],dp[1][i-1]+arr[i])
print(max(max(dp[0]),max(dp[1])))
