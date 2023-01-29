'''
퇴사 python 풀이
https://doctcoder.tistory.com/entry/%ED%87%B4%EC%82%AC-%ED%92%80%EC%9D%B4
'''
n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
dp=[0 for i in range(n+1)]
for i in range(n-1,-1,-1):
	if arr[i][0]+i>n:
		dp[i]=dp[i+1]
	else:
		dp[i]=max(dp[i+1],arr[i][1]+dp[i+arr[i][0]])
print(dp[0])
