'''
오르막 수 python 풀이
https://doctcoder.tistory.com/entry/%EC%98%A4%EB%A5%B4%EB%A7%89-%EC%88%98-%ED%92%80%EC%9D%B4
'''
n=int(input())
dp=[0 for i in range(n+1)]
dp[1]=10
for i in range(2,n+1):
	dp[i]=dp[i-1]*(i+9)//i
print(dp[n]%10007)
