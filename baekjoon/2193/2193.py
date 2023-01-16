'''
이친수 python 풀이
https://doctcoder.tistory.com/entry/%EC%9D%B4%EC%B9%9C%EC%88%98-%ED%92%80%EC%9D%B4
'''
dp=[0 for i in range(91)]
dp[1]=1
dp[2]=1
n=int(input())
for i in range(3,n+1):
	dp[i]=dp[i-1]+dp[i-2]
print(dp[n])
