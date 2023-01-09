'''
패션왕 신해빈 python 풀이
https://doctcoder.tistory.com/entry/%ED%8C%A8%EC%85%98%EC%99%95-%EC%8B%A0%ED%95%B4%EB%B9%88-%ED%92%80%EC%9D%B4
'''
from collections import Counter

t=int(input())
for i in range(t):
	n=int(input())
	cloth=[]
	for j in range(n):
		a,b=input().split()
		cloth.append(b)
	cnt=Counter(cloth)
	res=1
	for key in cnt:
		res*=cnt[key]+1
	print(res-1)
