'''
동물원 python 풀이
https://doctcoder.tistory.com/entry/%EB%8F%99%EB%AC%BC%EC%9B%90-%ED%92%80%EC%9D%B4
'''
n=int(input())
dp=[0 for i in range(n+1)]
dp[0]=1
dp[1]=3
for i in range(2,n+1):
	dp[i]=(2*dp[i-1]+dp[i-2])%9901
print(dp[n])
