'''
포도주 시식 python 풀이
https://doctcoder.tistory.com/entry/%ED%8F%AC%EB%8F%84%EC%A3%BC-%EC%8B%9C%EC%8B%9D-%ED%92%80%EC%9D%B4
'''
n=int(input())
arr=[0]
dp=[0]*(n+2)
for i in range(n):
	arr.append(int(input()))
arr.append(0)
dp[1]=arr[1]
dp[2]=dp[1]+arr[2]
for i in range(3,n+1):
	dp[i]=max(dp[i-1],dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i])
print(dp[n])
