'''
N과 M (12) python 풀이
https://doctcoder.tistory.com/entry/N%EA%B3%BC-M-12-%ED%92%80%EC%9D%B4
'''
from itertools import combinations_with_replacement

n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
res=list(set(combinations_with_replacement(arr,m)))
res.sort()
for i in res:
	for j in i:
		print(j,end=' ')
	print()
