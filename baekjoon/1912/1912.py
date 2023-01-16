'''
연속합 python 풀이
https://doctcoder.tistory.com/entry/%EC%97%B0%EC%86%8D%ED%95%A9-%ED%92%80%EC%9D%B4
'''
n=int(input())
arr=list(map(int,input().split()))
dp=[arr[i] for i in range(n)]
for i in range(1,n):
	dp[i]=max(dp[i],dp[i-1]+dp[i])
print(max(dp))
