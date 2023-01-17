'''
제곱수의 합 python 풀이
https://doctcoder.tistory.com/entry/%EC%A0%9C%EA%B3%B1%EC%88%98%EC%9D%98-%ED%95%A9-%ED%92%80%EC%9D%B4
'''
n=int(input())
dp=[i for i in range(n+1)]
for i in range(1,n+1):
	for j in range(1,i):
		if j**2>i: break
		if dp[i]>dp[i-j**2]+1: dp[i]=dp[i-j**2]+1
print(dp[n])
