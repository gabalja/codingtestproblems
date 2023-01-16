'''
가장 긴 증가하는 부분 수열 python 풀이
https://doctcoder.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%92%80%EC%9D%B4
'''
n=int(input())
arr=list(map(int,input().split()))
dp=[1 for i in range(1001)]
for i in range(1,n):
	for j in range(0,i):
		if arr[j]<arr[i]: dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
