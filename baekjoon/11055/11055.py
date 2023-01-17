'''
가장 큰 증가 부분 수열 python 풀이
https://doctcoder.tistory.com/entry/%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A6%9D%EA%B0%80-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%92%80%EC%9D%B4
'''
n=int(input())
arr=list(map(int,input().split()))
dp=[0 for i in range(1001)]
dp[0]=arr[0]
for i in range(1,n):
	for j in range(i):
		if arr[j]<arr[i]: dp[i]=max(dp[i],dp[j]+arr[i])
		else: dp[i]=max(dp[i],arr[i])
print(max(dp))
