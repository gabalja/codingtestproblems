'''
타일 채우기 python 풀이
https://doctcoder.tistory.com/entry/%ED%83%80%EC%9D%BC-%EC%B1%84%EC%9A%B0%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
n=int(input())
dp=[0 for i in range(31)]
dp[2]=3
for i in range(3,n+1):
	if i%2==0: dp[i]=3*dp[i-2]+2*sum(dp[:i-2])+2
print(dp[n])
