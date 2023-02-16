'''
부분수열의 합 python 풀이
https://doctcoder.tistory.com/entry/14225%EB%B2%88-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4%EC%9D%98-%ED%95%A9-%ED%92%80%EC%9D%B4
'''
from itertools import combinations

n=int(input())
s=list(map(int,input().split()))
nums=[0 for i in range(2000001)]
for i in range(1,n+1):
	a=combinations(s,i)
	for b in a:
		k=sum(b)
		nums[k]+=1
for i in range(1,2000001):
	if nums[i]==0:
		print(i)
		break
