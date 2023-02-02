'''
부분수열의 합 python 풀이
https://doctcoder.tistory.com/entry/%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4%EC%9D%98-%ED%95%A9-%ED%92%80%EC%9D%B4
'''
from itertools import combinations

n,s=map(int,input().split())
inp=list(map(int,input().split()))
cnt=0
for i in range(1,n+1):
	a=combinations(inp,i)
	for b in a:
		if sum(b)==s:
			cnt+=1
print(cnt)
